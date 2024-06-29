import React from 'react'
import Sidenav from '../../components/Sidenav'
import Navbar from '../../components/Navbar'
import Box from '@mui/material/Box';
//navegation
import Navigation from "../../components/Navigation";
//import TablaLotes from "../../components/corte/tablalotes";
import LotesTableC from '../../components/corte/comp/lotesview';

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
        <h3>Número de lotes por día en el mes</h3>
        {/*<TablaLotes />*/}
        <LotesTableC/>
      </Box>

    </Box>
      
    
      
    </>
  )
}