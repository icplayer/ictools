/*
 * Runtime for activities embedded in html page.
 * 
 * @author Krzysztof Langner
 */

function PlayerController() {
	
	var eventBus = new EventBus();
	
	this.getEventBus = function(){
		return eventBus;
	}
}