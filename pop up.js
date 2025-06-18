// <script type="text/javascript">
  //      function func () {
    //     alert("Hello")
     //}

     window.onload=function()
     {
         var el=document.getElementById('button');
         el.onclick=function(){
             var my_text=prompt('Enter text here');
             if(my_text) alert(my_text); // for example I've made an alert
         }
     }
     