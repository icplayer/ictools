var player;
function icOnAppLoaded(){
	$("#logger").append("<p>onAppLoaded</p>");
   	player = icCreatePlayer('_icplayer');
   	player.load('lesson2/pages/main.xml');
}

function log(text){
	$("#logger").append("<p>" + text + "</p>");
}

function clicked(){
	log("Button clicked");
	return false;
}
