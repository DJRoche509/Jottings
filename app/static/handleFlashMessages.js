// Wait for the document to be ready
$(document).ready(function () {
    // Select the flash messages container
    var flashMessages = $('#flash-messages');
    // Hide the flash messages after 5 seconds (5000 milliseconds)
    flashMessages.delay(5000).fadeOut('slow');
});


// wait for the document to be ready
// document.addEventListener('DOMContentLoaded', function () { 
//     // Select the flash messages container    
//     var flashMessages = document.getElementById('flash-messages'); 
//     //Hide the flash messages after 5 seconds(5000 milliseconds)    
//     setTimeout(function () {
//         flashMessages.style.display = 'none';
//     }, 5000);
//     console.log('JS script effected');
// });