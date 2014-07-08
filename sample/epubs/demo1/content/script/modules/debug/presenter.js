ModuleRuntime.registerModule("Debug", AddonDebug_create);

function AddonDebug_create(){
	
	var presenter = function(){}

	var outputView;
	var playerController;
	var eventBus;
	
	
	presenter.setPlayerController = function(service){
		this.playerController = service;
		this.eventBus = service.getEventBus();
	}
	
	presenter.onEventReceived = function(eventName, eventData){
	
		var html = 'Event: ' + eventName + "<br/> ";
		for(var key in eventData){
			html += key + ":" + eventData[key] + " | ";
		}
		outputView.innerHTML = html;
	}
	
	
	presenter.run = function(view, model){
		outputView = view;				
		this.eventBus.addEventListener('ItemSelected', this.onEventReceived);
		this.eventBus.addEventListener('ItemConsumed', this.onEventReceived);
		this.eventBus.addEventListener('ItemReturned', this.onEventReceived);
		this.eventBus.addEventListener('ValueChanged', this.onEventReceived);
		this.eventBus.addEventListener('Definition', this.onEventReceived);
		this.eventBus.addEventListener('AllOk', this.onEventReceived);
		this.eventBus.addEventListener('PageLoaded', this.onEventReceived);
		this.eventBus.addEventListener('ShowErrors', this.onEventReceived);
		this.eventBus.addEventListener('WorkMode', this.onEventReceived);
		this.eventBus.addEventListener('Reset', this.onEventReceived);
	}

	return presenter;
}
