$(document).ready(function(){

	const makeList = function(title){

	}


	$('.button').on('click', function(event){
		event.preventDefault();
		var title = $('.input').val()
		var url = 'https://en.wikipedia.org/w/api.php?action=opensearch&search='+title+'&format=json&callback=?'
		$('.bottom').empty()
		$.ajax(	
			{	
				url:url,
				type: 'GET',
				async: false,
				dataType: "json",
				success: function(result){
					console.log(result[1])
					var input = result[0];
					var titles = result[1];
					var descriptions = result[2];
					var links = result[3];
					console.log(links)
					var ul = $("<ul class='ul'></ul>")
					var len = titles.length;
					for(i=0;i<len;i++){
						var inp=$("<button type='button' value='Analyze' class='listButton'></button>");
						console.log(inp)
						var div=$("<div class='listDiv'><li class='list'><p>"+titles[i]+"</p><p>"+descriptions[i]+"</p><a href="+links[i]+">Link to:</a></li></div>");
						ul.append(div);
						div.append(inp);
					}
					var div = $('.bottom');
					div.removeClass('info');
					div.prepend(ul);

				} 

			}
		)
	})








});