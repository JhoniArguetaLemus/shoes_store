




const btn_open = document.getElementById('btnOpen');
const navbar=document.getElementById('navbar');
const close=document.getElementById('close')

btn_open.addEventListener('click', ()=>{

    navbar.classList.add('visible')
})

close.addEventListener('click', ()=>{
    navbar.classList.remove('visible');
    
})