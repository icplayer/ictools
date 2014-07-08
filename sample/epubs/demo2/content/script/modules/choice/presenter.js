ModuleRuntime.registerModule("Choice", Choice_create);

function Choice_create(){
	
	var presenter = function(){}
	var playerServices = null;
	var eventBus;
	var isMulti = false;
	var widgets = [];

	
	presenter.setPlayerController = function(services){
		this.playerServices = services;
		this.eventBus = this.playerServices.getEventBus();
	}
	
	
	presenter.run = function(view, model){
		isMulti = (model.isMulti == "true");
		createViewHtml(view, model);
		this._connectEvents();
	}
	
	
	function createViewHtml(element, model){
		element.id = model.id;
		for( var index in model.options){
			var option = model.options[index];
			var optionIndex = parseInt(index)+1;
			var optionId = model.id + "-" + optionIndex;
			var html = "<div id='" + optionId + "' ";
			if(isMulti){
				html += "class='ic_moption'>";
				html += "<input type='checkbox' name='" + model.id + "'/>";
			}
			else{
				html += "class='ic_soption'>";
				html += "<input type='radio' name='" + model.id + "'/>";
			}
			html += "<label for='" + optionId + "'>" + option.text + "</label></div>";
			$(html).appendTo(element);
			widgets.push(new OptionWidget(optionId, option.score, isMulti));
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

function OptionWidget(id, score, isMulti){
	var element = $('#' + id);
	var button = element.find('input:first');

	this.setWorkMode = function(){
		button.prop('disabled', false);
		element.removeClass(getBaseClass() + "-wrong");
		element.removeClass(getBaseClass() + "-correct");
	}
	
	this.setShowErrorsMode = function(){
		button.prop('disabled', true);
		if(button.is(':checked')){
			if(isCorrect()){
				element.addClass(getBaseClass() + "-correct");
			}
			else{
				element.addClass(getBaseClass() + "-wrong");
			}
		}
	}
	
	this.reset = function(){
		this.setWorkMode();
	}

	function isCorrect(){
		return score > 0;
	}
	
	function getBaseClass(){
		if(isMulti) return "ic_moption";
		else return "ic_soption";
	}

	return this;
}