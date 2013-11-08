var modelview_neuron_viewers = [];

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
    $('#' + tree_dialog).parent().addClass('no-close');
    
    // generate the tree
    AddTree(tree_dialog, modelview_build_tree_(modelview_data.tree));
    
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
        modelview_neuron_viewers.push(new_view_id);
        hide_dialog(new_view_id);
    });
    
    /*
    		    $('.treeButton').click(function() {
			    var windowID = $('#windowID').val();
			    AddTree(windowID, [
			        ['Animals', {callback: function() {console.log('Animals!');}, children:[
	                    ['Dogs', {callback: function() {console.log('Dogs!');}}],
	                    ['Cats'],
	                    ['Aardvarks']]}],
                    ['Plants', {callback: function() {console.log('Vegetables?');}, children:[
                        ['Tree'],
                        ['Arabidopsis']]}]]);
		    });
    */
});

function modelview_hide_all_() {
    var i, id;
    $.each(modelview_neuron_viewers, function (i, id) {
        hide_dialog(id);
    });
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
