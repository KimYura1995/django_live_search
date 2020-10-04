$(function() {
  $('#id_city').keyup(function() {
    console.log($('#id_city').val())
    ajaxLiveSearch();
  });
});

function ajaxLiveSearch() {
  $.ajax({
      type: 'GET',
      url: "/filter_city/",
      data: {
        'q' : $('#id_city').val(),
        'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val(),
      },
      success: function (response) {
        addCity(response);
      },
  });
}

function addCity(response) {
  let listCity = []
  for (airport of response) {
    if (!listCity.includes(airport.fields.city)) {
      listCity.push(airport.fields.city);
    }
  }
  $('#id_city').autocomplete({
    source: listCity,
  });
}
