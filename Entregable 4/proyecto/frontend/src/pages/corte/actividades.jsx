import React from 'react'
import Sidenav from '../../components/Sidenav'
import Navbar from '../../components/Navbar'
import Box from '@mui/material/Box';
//navegation
import Navigation from "../../components/Navigation";
//import TablaAct from "../../components/corte/tablaact";
import ActividadDiariaTable from '../../components/corte/comp/tablasact';

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
        <h3>Actividades que debe realizar la máquina en el día</h3>
        <ActividadDiariaTable/>

        
      </Box>

    </Box>
      
    
      
    </>
  )
}