ModuleRuntime.registerModule("Check", AddonCheck_create);

function AddonCheck_create(){
	
	var presenter = function(){}
	var playerServices = null;
	var eventBus;
	var isChecked = false;
	var button;

	
	presenter.setPlayerController = function(services){
		this.playerServices = services;
		this.eventBus = this.playerServices.getEventBus();
	}
	
	
	presenter.run = function(view, model){
		this.button = $(view.getElementsByTagName('button')[0]);
		var self = this;
		this.button.click(function(){
			self._clickHandler();
		});

	}
	
	presenter._clickHandler = function(){
		if(this.isChecked){
			this.eventBus.sendEvent("WorkMode", {});
			this.button.text("Check");
		}
		else{
			this.eventBus.sendEvent("ShowErrors", {});
			this.button.text("Uncheck");
		}
		this.isChecked = !this.isChecked;
	}

	
	return presenter;
}
