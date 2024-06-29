import React from 'react'
import Sidenav from '../../components/Sidenav'
import Navbar from '../../components/Navbar'
import Box from '@mui/material/Box';
//navegation
import Navigation from "../../components/Navigation";
//import Tabla from "../../components/corte/tabla";
//import OrdenesTable1 from '../../components/corte/pantalla1';
import App1 from '../../components/corte/pantalla1';

export default function OrdenCortePage() {
  return (
    <>
    <Navbar />
    <Box height={30}/>
    <Box sx={{ display: 'flex' }}>
      <Sidenav/>
      
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
       <h1>Área de Corte</h1> 
       <div>
            <Navigation />{" "}
          </div>
        <h3>Orden de producción</h3>
        {/*<Tabla />*/}
        <Box><App1 /></Box>
        
      </Box>


      
    </Box>
      
    
      
    </>
  )
}