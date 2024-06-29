import React from 'react'
import Sidenav from '../../components/Sidenav'
import Navbar from '../../components/Navbar'
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import RegCant1 from '../../components/confeccion/regcant1';

export default function GuiaPage() {
  return (
    <>
    <Navbar />
    <Box height={30}/>
    <Box sx={{ display: 'flex' }}>
      <Sidenav/>
      
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
       <h1>Área de Confección</h1> 
        <Typography paragraph>
          resumen
        </Typography>
        <h3>
          Órdenes asignadas
        </h3>
        
      <div><RegCant1 /></div>
      </Box>

    </Box>
      
    
      
    </>
  )
}