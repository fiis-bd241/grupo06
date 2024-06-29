import React from 'react'
import Sidenav from '../../components/Sidenav'
import Navbar from '../../components/Navbar'
import Box from '@mui/material/Box';
//navegation
import Navigation from "../../components/Navigation";
//import TablaActMaq from "../../components/corte/tablaactmaq";
import ActivitiesTable from '../../components/corte/comp/tablaactividad';

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
        <h3>Actividades diarias por máquina</h3>
        {/*<TablaActMaq />*/}
        <ActivitiesTable/>
      </Box>

    </Box>
      
    
      
    </>
  )
}