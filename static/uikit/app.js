// // Invoke Functions Call on Document Loaded
// document.addEventListener('DOMContentLoaded', function () {
//   hljs.highlightAll();
// });


// let alertWrapper = document.querySelector('.alert')
// let alertClose = document.querySelector('.alert__close')

// if (alertWrapper) {
//   alertClose.addEventListener('click', () =>
//     alertWrapper.style.display = 'none'
//   )
// app.js}
document.addEventListener('DOMContentLoaded', function () {
  console.log("JavaScript is working");
  hljs.highlightAll();

  let alertWrapper = document.querySelector('.alert');
  let alertClose = document.querySelector('.alert__close');

  if (alertWrapper && alertClose) {
    alertClose.addEventListener('click', () => {
      alertWrapper.style.display = 'none';
    });
  }
});


