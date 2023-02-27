$(document).ready(function () {
    $('#example').DataTable();
});

const button = document.getElementById('#btn');

const disableButton = () => {
    console.log("va");
    button.disabled = true;

};

button.addEventListener('click', disableButton);