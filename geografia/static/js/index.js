let ciudades = [];
const listarCiudades = async (idPais)=>{
    try{
        const response = await fetch(`./ciudades/${idPais}`);
        const data = await response.json();
        
        if(data.message == "Success"){
            ciudades = data.ciudades;
            let opciones;
            ciudades.forEach(ciudad => {
                opciones += `<option value='${ciudad.id}'>${ciudad.nombre}</option>`
            });
            cboCiudad.innerHTML = opciones;
            mostarAlcalde(ciudades[0].id);
        }else{
            alert('Paises no encontrados')
        }
    }catch(err){
        console.log(err);
    }
}

const listarPaises = async ()=>{
    try{
        const response = await fetch("./paises");
        const data = await response.json();
        
        if(data.message == "Success"){
            let opciones;
            data.paises.forEach(pais => {
                opciones += `<option value='${pais.id}'>${pais.nombre}</option>`
            });
            // En las ultimas versiones de js y html los id ya se convierten
            // en variables que ya podemos utilizar sin un getElementById()
            cboPais.innerHTML = opciones;
            listarCiudades(data.paises[0].id);
        }else{
            alert('Paises no encontrados')
        }
    }catch(err){
        console.log(err);
    }
}

const mostarAlcalde = async (idCiudad)=>{
    let alcalde = ciudades.filter(ciudad =>ciudad.id == idCiudad)[0].alcalde;
    txtAlcalde.style.animation = "aparecer 1s forwards";
    document.querySelector(".selectores").style.animation = "fondo 1.5s forwards"
    txtAlcalde.textContent = `Alcalde: ${alcalde}`;
    await setTimeout(()=>{
        txtAlcalde.style.animation = "";
        document.querySelector(".selectores").style.animation = "";
    }, 1000)
}

const cargaInicial = async ()=>{

    await listarPaises();
    cboPais.addEventListener("change", (e)=>{
        listarCiudades(e.target.value);
    })

    cboCiudad.addEventListener("change", e=>{
        mostarAlcalde(e.target.value);
    })
}

addEventListener("load", async ()=>{
    

    await cargaInicial();
})