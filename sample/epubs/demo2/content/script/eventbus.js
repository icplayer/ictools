/*
 * Event bus implementation
 * 
 * @author Krzysztof Langner
 */

function EventBus() {

	var handlers = {}
	
	this.addEventListener = function(eventName, handler){
		var eventHandlers = handlers[eventName] || [];
		eventHandlers.push(handler);
		handlers[eventName] = eventHandlers;
	}
	
	this.sendEvent = function(eventName, eventData){
		var eventHandlers = handlers[eventName] || [];
		for(var i in eventHandlers){
			eventHandlers[i](eventName, eventData);
		}
	}
	
	this.reset = function(){
		handlers = {};
	}
}