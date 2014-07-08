ModuleRuntime.registerModule("Text", AddonText_create);

function AddonText_create(){
	
	var presenter = function(){}
	var playerServices = null;
	var eventBus;
	var widgets = [];

	
	presenter.setPlayerController = function(service){
		this.playerController = service;
		this.eventBus = service.getEventBus();
		this._connectEvents();
	}
	
	
	presenter.run = function(view, model){
		var parsedText = parseText(model.text, model.id);
		view.innerHTML = parsedText.text;
		for(var i in parsedText.gaps){
			var gap = parsedText.gaps[i];
			widgets.push(new GapWidget(gap.id, gap.answer));
		}
		for(var i in parsedText.choices){
			var choice = parsedText.choices[i];
			widgets.push(new ChoiceWidget(choice.id, choice.answer));
		}
	}

	
	presenter._connectEvents = function(){
		this.eventBus.addEventListener('ShowErrors', this.setShowErrorsMode);
		this.eventBus.addEventListener('WorkMode', this.setWorkMode);
		this.eventBus.addEventListener('Reset', this.reset);
	}
	
	 presenter.setWorkMode = function () {
		 for(var i in widgets){
			 var gap = widgets[i];
			 gap.setWorkMode();
		 }
	 }

	 presenter.setShowErrorsMode = function () {
		 for(var i in widgets){
			 var gap = widgets[i];
			 gap.setShowErrorsMode();
		 }
	 }

	 presenter.reset = function () {
		 for(var i in widgets){
			 var gap = widgets[i];
			 gap.reset();
		 }
	 }

	return presenter;
}


function GapWidget(id, answer){
	var element = $('#' + id);

	this.setWorkMode = function(){
		element.prop('disabled', false);
		element.removeClass("ic_gap-wrong");
		element.removeClass("ic_gap-correct");
	}
	
	this.setShowErrorsMode = function(){
		element.prop('disabled', true);
		if(isCorrect()){
			element.addClass("ic_gap-correct");
		}
		else{
			element.addClass("ic_gap-wrong");
		}
	}
	
	this.reset = function(){
		this.setWorkMode();
	}
	
	function isCorrect(){
		var text = element.val();
		return text == answer;
	}

	return this;
}


function ChoiceWidget(id, answer){
	var element = $('#' + id);

	this.setWorkMode = function(){
		element.prop('disabled', false);
		element.removeClass("ic_inlineChoice-wrong");
		element.removeClass("ic_inlineChoice-correct");
	}
	
	this.setShowErrorsMode = function(){
		element.prop('disabled', true);
		if(isCorrect()){
			element.addClass("ic_inlineChoice-correct");
		}
		else{
			element.addClass("ic_inlineChoice-wrong");
		}
	}
	
	this.reset = function(){
		this.setWorkMode();
	}

	function isCorrect(){
		var text = element.val();
		return text == answer;
	}

	return this;
}