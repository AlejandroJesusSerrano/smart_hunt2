import Swal from '../lib/sweetalert2-11.10.6/sweetalert2.all.min'
import '../lib/sweetalert2-11.10.6/sweetalert2.min.css'

function swalError(){
  Swal.fire({
    icon: "error",
    title: "Oops...",
    text: "Something went wrong!",
    footer: '<a href="#">Why do I have this issue?</a>'
  });
}