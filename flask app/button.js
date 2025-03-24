var redButton = $("#red_button");
redButton.click(function() {
	console.log(redButton.text());
	if (redButton.text() === "Red LED On") {
		$.ajax({
			url: "/redled_on",
			type: "post",
			success: function(response) {
				console.log(response);
				redButton.text("Red LED Off");
			}
		});
	}
	else {
		$.ajax({
			url: "/redled_off",
			type: "post",
			success: function() {
				redButton.text("Red LED On");
			}
		})
	}
});
yellowButton.click(function() {
	console.log(yellowButton.text());
	if (yellowButton.text() === "Yellow LED On") {
		$.ajax({
			url: "/yellowled_on",
			type: "post",
			success: function(response) {
				console.log(response);
				yellowButton.text("Yellow LED Off");
			}
		})
	}
	else {
		$.ajax({
			url: "/yellowled_off",
			type: "post",
			success: function() {
				yellowButton.text("Yellow LED On");
			}
		})
	}
});
