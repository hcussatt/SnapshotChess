var photoButton = $("#photo_button");
photoButton.click(function() {
    $.ajax({
        url: "/photo",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
	
});