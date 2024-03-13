$(function(){
console.log('executing... datatables.ajax.script')
  $('#data').DataTable({
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender:true,
    language: {
    url: '/static/lib/datatables_2.0.1/spanish.json'
    },
    ajax: {
      url: '/sh/province/list/',
      type: 'POST',
      data: {
        'action':'searchdata'
      },
      dataSrc: ""
    },
    columns: [
      {'data': 'id' },
      {'data': 'number_id'},
      {'data': 'province'},
      {'data': 'date_creation'},
      {'data': 'date_updated'},
    ],
    columnDefs: [
      {
        targets: [2],
        class: 'text-center',
        orderable: false,
        render: function(data, type, row) {
          let buttons = '<a href="/sh/province/update/'+row.id+'/" class="btn btn-warning btn-sm" alt="Editar"><i class="bi-pen small"></i></a> ';
          buttons += '<a href="/sh/province/delete/'+row.id+'/" class="btn btn-danger btn-sm" alt="Borrar"><i class="bi-trash3 small"></i></a>';
          return buttons
        }
      },
    ],
    initComplete: function (settings, json) {
    }
  });

});