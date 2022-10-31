require([
    "splunkjs/mvc",
    "splunkjs/mvc/simplexml/ready!"
], function(mvc) {
	console.log("loaded")
    $('button').on("click", function(e) {
        // find text field with id starting with yourfieldid
		console.log("clicked")
        $('[aria-label="Name"]:text').val("")
    });        

});