/*
 * Parser for interactive text
 * 
 * @author Krzysztof Langner
 */

function parseText(inputText, baseId) {
	var idCounter = 1;
	var gaps = [];
	var choices = [];
	var text = parse(inputText);
	return {text: text, gaps: gaps, choices: choices};
	
	
	function parse(text){
		var parsed = parseGaps(text);
		return parseChoices(parsed);
	}
	
	function parseGaps(text){
		var input = text;
		var output = "";
		var index = 0; 
		while((index = input.indexOf("\\gap{")) >= 0){
			output = input.substring(0, index);
			input = input.substring(index+5);
			var end = input.indexOf("}");
			var answers = input.substring(0, end);
			var id = getNextId();
			var html = "<input id='" + id + "' type='edit' class='ic_gap'/>";
			output += html;
			gaps.push({id: id, answer: answers});
			input = input.substring(end+1);
		}
		return output + input;
	}
	
	function parseChoices(text){
		var input = text;
		var output = "";
		var index = 0; 
		while((index = input.indexOf("\\choice{")) >= 0){
			output = input.substring(0, index);
			input = input.substring(index+8);
			var end = input.indexOf("}");
			var options = input.substring(0, end).split("|");
			var answer = options[0];
			var sorted = options.sort();
			var id = getNextId();
			var html = "<select id='" + id + "' class='ic_inlineChoice'>";
			html += "<option value='-'>---</option>"
			for(var index in options){
				var value = options[index];
				html += "<option value='" + value + "'>"+ value + "</option>";
			}
			html += "</select>";
			output += html;
			choices.push({id: id, answer: answer});
			input = input.substring(end+1);
		}
		return output + input;
	}
	
	function getNextId(){
		var id = baseId + "-" + idCounter;
		idCounter += 1;
		return id;
	}
}

