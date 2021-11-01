window.onload = function () {


    var date = new Date();
    document.getElementById('date').innerHTML = date.getFullYear();
    let vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);

    //To prevent zoom in mobile
    window.addEventListener('resize', () => {
        // We execute the same script as before
        let vh = window.innerHeight * 0.01;
        document.documentElement.style.setProperty('--vh', `${vh}px`);
      });
      
    //Nav background change on sudden scroll
    if (document.body.scrollTop >= 30 || document.documentElement.scrollTop >= 30 ){
        document.querySelector('nav').classList.add('nav-open')
    }
    else{
        document.querySelector('nav').classList.remove('nav-open')
    }

    //Nav close on main click
    document.querySelector('main').addEventListener('click',()=>{
        document.getElementById('nav').classList.remove('open')
        document.getElementById('toggler').classList.remove('current')
    })

    //Nav close on footer click
    document.querySelector('footer').addEventListener('click',()=>{
        document.getElementById('nav').classList.remove('open')
        document.getElementById('toggler').classList.remove('current')
    })

    //Nav implementation
    document.getElementById('toggler').addEventListener('click',()=>{
        // console.log('open')
        document.getElementById('nav').classList.toggle('open')
        document.getElementById('toggler').classList.toggle('current')
        if (document.body.scrollTop < 30 && document.documentElement.scrollTop < 30 ){
            if(document.getElementById('nav').classList.contains('open')){
                document.getElementById('nav').classList.add('nav-open')
            }
            else{
                setTimeout(() => {
                    document.getElementById('nav').classList.remove('nav-open')
                }, 300);
            }
        }
    })
}

//Nav background on scroll
document.onscroll = function () {
    // console.log(this.documentElement.scrollTop)
    document.getElementById('nav').classList.remove('open')
    document.getElementById('toggler').classList.remove('current')
    if (document.body.scrollTop >= 30 || document.documentElement.scrollTop >= 30 ){
        document.querySelector('nav').classList.add('nav-open')
    }
    else{
        document.querySelector('nav').classList.remove('nav-open')
    }
}

//Text area height
$("textarea").each(function () {
    this.setAttribute("style", "height:" + (this.scrollHeight) + "px;overflow-y:hidden;");
  }).on("input", function () {
    this.style.height = "auto";
    this.style.height = (this.scrollHeight) + "px";
  });

    let forms = document.querySelectorAll('form');
  
    forms.forEach( function(e) {
      e.addEventListener('submit', function(event) {
        event.preventDefault();
  
        let thisForm = this;
  
        let action = thisForm.getAttribute('action');
  
        let formData = new FormData( thisForm );
        submitForm(thisForm, action, formData);
    //     if ( recaptcha ) {
    //       if(typeof grecaptcha !== "undefined" ) {
    //         grecaptcha.ready(function() {
    //           try {
    //             grecaptcha.execute(recaptcha, {action: 'php_email_form_submit'})
    //             .then(token => {
    //               formData.set('recaptcha-response', token);
    //               php_email_form_submit(thisForm, action, formData);
    //             })
    //           } catch(error) {
    //             displayError(thisForm, error)
    //           }
    //         });
    //       } else {
    //         displayError(thisForm, 'The reCaptcha javascript API url is not loaded!')
    //       }
    //     } else {
    //       php_email_form_submit(thisForm, action, formData);
    //     }
    //   });
    });
})
  
function submitForm(thisForm, action, formData) {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    console.log(thisForm.elements[0])
    thisForm.elements[0].value = 'Please wait....'
    thisForm.elements[0].classList.replace('message-close','message-info')
    thisForm.elements[thisForm.elements.length -1].disabled = true;
    // console.log(thisForm.elements.length)
    var obj = {}
    for(var i=0; i< thisForm.elements.length;i++){
        // console.log(i)
        // console.log(thisForm.elements[i])
        obj[thisForm.elements[i].name] = thisForm.elements[i].value
    }
    console.log(obj)
    $.ajax({
        url: action,
        type: "POST",
        headers: {'Content-Type':'application/json','X-CSRFToken': csrftoken},
        data: JSON.stringify(obj),
        contentType: "application/json; charset=utf-8",
        success: function(resp){
            if(resp.error){
                // console.log(error)
                // console.log(resp.message)
                thisForm.elements[0].value = resp.message
                thisForm.elements[0].classList.replace('message-info','message-error')
                thisForm.elements[thisForm.elements.length -1].disabled = false;
            }
            else{
                // console.log(resp.message)
                thisForm.elements[0].value = resp.message
                thisForm.elements[0].classList.replace('message-info','message-success')
                thisForm.elements[thisForm.elements.length -1].disabled = false;
                thisForm.reset()
            }
        },
        error: ()=> {
            // console.log('hellp')
            thisForm.elements[0].value = 'Something went wrong'
            thisForm.elements[0].classList.replace('message-info','message-error')
            thisForm.elements[thisForm.elements.length -1].disabled = false;
        }
    });


    // fetch(action, {
    // method: 'POST',
    // body: formData,
    // headers: {'X-Requested-With': 'XMLHttpRequest'},
    // dataT
    // })
    // .then(response => {
    // if( response.ok ) {
    //     console.log(response)
    // } else {
    //     throw new Error(`${response.status} ${response.statusText} ${response.url}`); 
    // }
    // })
    // .then(data => {
    //     console.log(data)
    // thisForm.querySelector('.loading').classList.remove('d-block');
    // if (data.trim() == 'OK') {
    //     thisForm.querySelector('.sent-message').classList.add('d-block');
    //     thisForm.reset(); 
    // } else {
    //     throw new Error(data ? data : 'Form submission failed and no error message returned from: ' + action); 
    // }
    // })
    // .catch((error) => {
    // var errl = error.toString()
    // console.log(errl.substring(7,error.length))
    // if(errl.substring(7,error.length) === 'done'){
    //     console.log('aha')
    //     displaySuccess(thisForm, 'Successfully Sent')
    //     thisForm.reset()
    // }
    // else{
    //     displayError(thisForm, 'Sec ' +error);
    // }
    // });
}
  
    // function displayError(thisForm, error) {
        
    // }
    // function displaySuccess(thisForm, suc) {
        
    // }
  
//   })();
  









//Service worker
// var serviceWorkerPath = "/charcha-serviceworker.js";
// var charchaServiceWorker = registerServiceWorker(serviceWorkerPath);
// function registerServiceWorker(serviceWorkerPath){
//    if('serviceWorker' in navigator){
//      navigator.serviceWorker
//        .register("/charcha-serviceworker.js")
//          .then(function(reg){ console.log('Service Worker done');})
//          .catch(function(error){console.log(error)});
//    }
// }