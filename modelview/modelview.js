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


function modelview_build_tree_(src_tree) {
    var result = [];
    $.each(src_tree, function (i, row) {
        children = undefined;
        if (row.children != undefined) {
            children = modelview_build_tree_(row.children);
            if (children.length == 0) children = undefined;
        }
        result.push([row.text, {children: children}]);
    });
    return result;
}
