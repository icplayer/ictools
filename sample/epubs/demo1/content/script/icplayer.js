/*
 * Runtime for activities embedded in html page.
 * 
 * @author Krzysztof Langner
 */

var ModuleRuntime = {
	factories: {},
	playerController: new PlayerController(),
	
	registerModule: function(typeName, presenter){
		this.factories[typeName] = presenter
	},
	
	run: function(){
		this._initModules();
	},
	
	_initModules: function(){
		for(var name in this.factories){
			var factory = this.factories[name];
			this._loadFactoryModules(name, factory);
		}
	},
	
	_loadFactoryModules: function(name, factory){
		var query = "div[module='" + name + "']";
		var _this = this;
		$(query).each(function(e){
			_this._loadModule(this, factory);
		});
	},
	
	_loadModule: function(element, factory){
		var model = this._initModel(element);
		$(element).children("model").remove();
		var presenter = factory();
		presenter.setPlayerController(this.playerController);
		presenter.run(element, model);
	},
	
	_initModel: function(element){
		var model = loadModel($(element).children("model")[0]);
		return model;
	}
	
}


function loadModel(modelElement){
	var model = {};
	var propertyNodes = $(modelElement).find("property");
	propertyNodes.each(function(){
		var name = $(this).attr("name");
		var value = $(this).attr("value");
		var type = $(this).attr("type");
		if(type == "list"){
			var items = $(this).find("item");
			var properties = [];
			$(this).find("item").each(function(){
				properties.push(loadModel(this));
			});
			model[name] = properties;
		}
		else if(value != null){
			model[name] = value;
		}
		else{
			model[name] = $(this).text();
		}
	
	});
	return model;
}


$(function() {
	ModuleRuntime.run();
});