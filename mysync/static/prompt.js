$(document).ready(function() {

    var items=[];
    function loadOptions(){
      $.getJSON('/items', function(data, status, xhr){
          for (var i =0; i < data.length; i++ ) {
            items.push(data[i].item);
            }

      });
    };
    loadOptions();

    $('#option').autocomplete({
      source: items,
    });



});
