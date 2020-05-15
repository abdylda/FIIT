$(document).ready(function(){
  var table = $('#table').DataTable();
  console.log(table)
  $('#btn-export').on('click', function(){
      $('<table>').append(table.$('tr').clone()).table2excel({
          exclude: ".excludeThisClass",
          name: "Worksheet Name",
          filename: "SomeFile" //do not include extension
      });
  });
})