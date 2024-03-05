
    let spanish = require("{% static 'lib/datatables_2.0.1/spanish.json' %}")

    let table = new DataTable('#data', {
      responsive: true,
      languge: spanish
    });
