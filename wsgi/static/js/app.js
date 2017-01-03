$(document).ready(function() {
    $('select').material_select();
  });
$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year
    format: 'yyyy-mm-dd'
});

$(document).ready(function(){
    $('.tooltipped').tooltip({delay: 50, html:true});
});

$(document).ready(function(){
    // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
    $('.modal-trigger').leanModal();
});

function submitform()
{
    document.forms["levantamento-edit"].submit();
}