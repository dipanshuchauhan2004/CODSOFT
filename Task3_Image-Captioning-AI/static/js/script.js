const imageInput = document.getElementById("imageInput");
const chooseBtn = document.getElementById("chooseBtn");
const dropArea = document.getElementById("drop-area");
const preview = document.getElementById("preview");

const generateBtn = document.getElementById("generate");
const copyBtn = document.getElementById("copy");
const downloadBtn = document.getElementById("download");
const resetBtn = document.getElementById("reset");

const caption = document.getElementById("caption");
const loader = document.getElementById("loader");

let selectedFile = null;

/* -----------------------------
   Choose Button
------------------------------*/

chooseBtn.addEventListener("click", () => {

    imageInput.click();

});


/* -----------------------------
   File Selected
------------------------------*/

imageInput.addEventListener("change", () => {

    if(imageInput.files.length > 0){

        selectedFile = imageInput.files[0];

        previewImage(selectedFile);

    }

});


/* -----------------------------
   Drag & Drop
------------------------------*/

dropArea.addEventListener("dragover",(e)=>{

    e.preventDefault();

    dropArea.classList.add("dragover");

});

dropArea.addEventListener("dragleave",()=>{

    dropArea.classList.remove("dragover");

});

dropArea.addEventListener("drop",(e)=>{

    e.preventDefault();

    dropArea.classList.remove("dragover");

    if(e.dataTransfer.files.length>0){

        selectedFile=e.dataTransfer.files[0];

        previewImage(selectedFile);

    }

});


/* -----------------------------
   Preview
------------------------------*/

function previewImage(file){

    const reader=new FileReader();

    reader.onload=function(e){

        preview.src=e.target.result;

        preview.style.display="block";

    }

    reader.readAsDataURL(file);

}


/* -----------------------------
   Generate Caption
------------------------------*/

generateBtn.addEventListener("click",async()=>{

    if(selectedFile==null){

        alert("Please Select an Image");

        return;

    }

    loader.style.display="block";

    caption.innerHTML="Generating Caption...";

    const formData=new FormData();

    formData.append("image",selectedFile);

    try{

        const response=await fetch("/generate-caption",{

            method:"POST",

            body:formData

        });

        const data=await response.json();

        loader.style.display="none";

        if(data.error){

            caption.innerHTML=data.error;

            return;

        }

        caption.innerHTML=data.caption;

    }

    catch(error){

        loader.style.display="none";

        caption.innerHTML="Unable to connect to Python Server.";

    }

});


/* -----------------------------
   Copy Caption
------------------------------*/

copyBtn.addEventListener("click",()=>{

    if(caption.innerHTML==="Your caption will appear here..."){

        return;

    }

    navigator.clipboard.writeText(caption.innerHTML);

    alert("Caption Copied");

});


/* -----------------------------
   Download Caption
------------------------------*/

downloadBtn.addEventListener("click",()=>{

    if(caption.innerHTML==="Your caption will appear here..."){

        return;

    }

    const blob=new Blob([caption.innerHTML],{

        type:"text/plain"

    });

    const link=document.createElement("a");

    link.href=URL.createObjectURL(blob);

    link.download="caption.txt";

    link.click();

});


/* -----------------------------
   Reset
------------------------------*/

resetBtn.addEventListener("click",()=>{

    selectedFile=null;

    imageInput.value="";

    preview.src="";

    preview.style.display="none";

    caption.innerHTML="Your caption will appear here...";

});