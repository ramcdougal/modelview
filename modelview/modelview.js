var modelview_neuron_viewers = [];

var last_right, last_top;

function reposition_dialog(id) {
    // set next to the last positioned dialog
    var doc_width = document.width;
    var me = $('#' + id);
    var mep = me.parent();
    mep.offset({left: last_right + 10, top: last_top});

    // except: drop down if too far to the right
    if (mep.offset().left + mep.outerWidth() > doc_width) {
        mep.offset({left: 20, top: last_top + 100});
    }
    last_top = mep.offset().top;
    last_right = mep.offset().left + mep.outerWidth();
}

$(function() {
    if (modelview_data.title != undefined) {
        document.title = 'ModelView: ' + modelview_data.title;
    } else {
        document.title = 'ModelView';
        modelview_data.title = 'ModelView';
    }
    
    if (modelview_data.short_title == undefined) {
        modelview_data.short_title = modelview_data.title;
    }
    
    // create a dialog for the tree with no close box
    tree_dialog = MakeDialog(modelview_data.short_title, true);
    var tree_dialog_handle = $('#' + tree_dialog);
    tree_dialog_handle.parent().addClass('no-close');
    
    // generate the tree
    AddTree(tree_dialog, modelview_build_tree_(modelview_data.tree));

    // start with a fixed initial height for this dialog.
    // the user can still resize it, but this prevents it from growing when the
    // tree is expanded
    var spacing = tree_dialog_handle.parent().height() - tree_dialog_handle.height()
    // start at 2/3 of the height. arbitrary.
    tree_dialog_handle.parent().height(document.height * 0.66);
    tree_dialog_handle.height(tree_dialog_handle.parent().height() - spacing);
    
    // position it somewhere better
    tree_dialog_handle.parent().css('top', '1em');
    tree_dialog_handle.parent().css('left', '1em');

    last_top = tree_dialog_handle.parent().offset().top;
    last_right = tree_dialog_handle.parent().offset().left + tree_dialog_handle.parent().outerWidth();
    
    last_positioned_dialog = tree_dialog;
    
    // open all links in new window, based on http://trevordavis.net/blog/use-jquery-to-open-all-external-links-in-a-new-window
    $('a').attr('target', '_blank');
    
    // setup the neuron views
    if (modelview_data.neuron == undefined) {
        modelview_data.neuron = [];
    }

    if (modelview_data.neuronviewer == undefined) {
        modelview_data.neuronviewer = [];
    }
    
    $.each(modelview_data.neuronviewer, function(i, neuron_view) {
        var neuron_data = modelview_data.neuron[neuron_view];
        var new_view_id = MakeNeuronViewer(neuron_data.title, neuron_data.morphology);
        reposition_dialog(new_view_id);
        modelview_neuron_viewers.push(new_view_id);
        hide_dialog(new_view_id);
    });
    
    // flot dialog
    flot_dialog = MakeDialog(modelview_data.short_title, true);
    $('#' + flot_dialog).parent().addClass('no-close');
    counter++;
    flot_title = AddComponent(flot_dialog, '<div style="text-align: center;" id=' + counter + '>title</div>');
    flot_fig = AddChart(flot_dialog, {contextmenu: false, doplot: false});
    plottedFlot['placeholder' + flot_fig] = $.plot($('#placeholder' + flot_fig), []);
    $('#' + flot_dialog).resize(function() {
        $('#placeholder' + flot_fig).height(max(300, $('#' + flot_dialog).height() - $('#' + flot_title).height() - 50));
        plottedFlot['placeholder' + flot_fig].draw();
    });
    reposition_dialog(flot_dialog);
    hide_dialog(flot_dialog);

});

function show_flot_(data, title, xaxes, yaxes) {
    if (!xaxes.length) xaxes = undefined;
    if (!yaxes.length) yaxes = undefined;
    if (title == undefined) title = '';
    show_dialog(flot_dialog);
    $('#' + flot_title)[0].innerHTML = title;
    plottedFlot['placeholder' + flot_fig] = $.plot($('#placeholder' + flot_fig), data, {zoom: {interactive: true}, pan: {interactive: true}, xaxes: xaxes, yaxes: yaxes});
}

function modelview_hide_all_() {
    var i, id;
    $.each(modelview_neuron_viewers, function (i, id) {
        hide_dialog(id);
    });
    hide_dialog(flot_dialog);
}

function modelview_build_tree_(src_tree) {
    var result = [];
    var f, i, j;
    $.each(src_tree, function (i, row) {
        children = undefined;
        if (row.children != undefined) {
            children = modelview_build_tree_(row.children);
            if (children.length == 0) children = undefined;
        }
        if (row.action != undefined) {
            f = function() {
                modelview_hide_all_();
                $.each(row.action, function (j, action) {
                    if (action.kind == 'neuronviewer') {
                        var id = modelview_neuron_viewers[action.id];
                        show_dialog(id);
                        set_neuron_markers(id, action.markers);
                        set_neuron_colors(id, action.colors);
                    } else if (action.kind == 'flot') {
                        show_flot_(action.data, action.title, action.xaxes, action.yaxes);
                    } else {
                        console.log('ignoring unknown action kind: ' + action.kind);
                    }
                });
            }
        } else {
            f = modelview_hide_all_;
        }
        result.push([row.text, {children: children, callback: f}]);
    });
    return result;
}
