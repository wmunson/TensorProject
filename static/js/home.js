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
						var inp=$("<button type='button' class='listButton' data-id='"+i+"'>Analyze</button>");
						console.log(inp)
						var div=$("<div class='listDiv remove'><li class='list'><h3>"+titles[i]+"</h3><p>"+descriptions[i]+"</p><a id='"+i+"' href="+links[i]+">Link to:</a></li></div>");
						ul.append(div);
						div.append(inp);
						makeEvent(inp);
					}
					var div = $('.bottom');
					div.removeClass('info');
					div.prepend(ul);

				} 

			}
		)
	})



	var makeEvent = function(but){
		but.on('click', function(event){
			console.log('click')
			var parent = $(this).parent()
			parent.removeClass('remove')
			$('.remove').fadeOut(500);
			$('.remove').animate({
				'opacity':'0',
				},
				{
				'complete':function(){
					$('.remove').remove()
					}	
				})

			parent.animate({
				'top':'-=40em'
			},'slow');
			
			// console.log(parent)
			var id = this.dataset.id
			var link = $('#'+id)[0].href;
			var url = 'http://localhost:8000/analyze?link='+link
			var mainDiv = $('.lists');
			var h = $('<h2 class="h">Running Analysis. Please be Patient</h2>')
			var newDiv = $('<div class = "loader"><div class="loading-bar"></div><div class="loading-bar"></div><div class="loading-bar"></div><div class="loading-bar"></div><div class="loading-bar"></div></div>')
			mainDiv.append(h)
			mainDiv.append(newDiv)
			$.ajax(
				{
					url: url,
					type:'GET',
					// async:false,
					dataType:'json',
					success: function(result){
						console.log(result)
						$('.loader').remove()
						$('.h').remove()
						
						var descDiv = $('<div id="titleDiv"><h2class="h2">Sentiment Rating:</h2> <h3 class="h3">0~Negative, 100~Positive:</h3></div>');
						var graphDiv = $('<div id="chart"></div>');
						var countDiv = $('<div id="count"></div>');
						var resultDiv = $('<div class="results"></div>');
						count = $('<h2class="h2">Words in Article:</h2><h3 class="h3">'+result['words']+'</h3>');
						countDiv.append(count);
						descDiv.append(graphDiv);
						resultDiv.append(descDiv);
						resultDiv.append(countDiv);
						mainDiv.append(resultDiv);
						sent = result['result'];
						makeGraph(sent);
					}
				}

			)
		})
	}

	// ////////////////////////
	//////// gauge chart ////////

	require.config({
			baseUrl: '/js',
			paths: {
    		d3: "http://d3js.org/d3.v3.min"
  			}
		});

	const makeGraph = function(val){
	var value = val*7;
	require(["d3", "c3"], function(d3, c3) {

	var chart = c3.generate({
	    bindto:'#chart',
	    data: {
	        columns: [
	            ['data', value]
	        ],
	        type: 'gauge',
	        onclick: function (d, i) { console.log("onclick", d, i); },
	        onmouseover: function (d, i) { console.log("onmouseover", d, i); },
	        onmouseout: function (d, i) { console.log("onmouseout", d, i); }
	    },
	    gauge: {
	//        label: {
	//            format: function(value, ratio) {
	//                return value;
	//            },
	//            show: false // to turn off the min/max labels.
	//        },
	//    min: 0, // 0 is default, //can handle negative min e.g. vacuum / voltage / current flow / rate of change
	//    max: 100, // 100 is default
	//    units: ' %',
	//    width: 39 // for adjusting arc thickness
	    },
	    color: {
	        pattern: ['#FF0000', '#F97600', '#F6C600', '#60B044'], // the three color levels for the percentage values.
	        threshold: {
	//            unit: 'value', // percentage is default
	//            max: 200, // 100 is default
	            values: [30, 60, 90, 100]
	        }
	    },
    	size: {
        	height: 180
    	}
		});
		});
		}






});