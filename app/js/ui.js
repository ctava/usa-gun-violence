$( "#date" ).datepicker({
	inline: true
});

$( "#datepicker" ).datepicker({
	inline: true
});

$("#dp").datepicker({
	ShowOn: "button",
	buttonImage: "img/ui-icons_228ef1_256x240.png",
	buttonImageOnly: true,
	onSelect:function(selectedDate) {
		Console.log(selectedDate);
	},
	inline: true
});