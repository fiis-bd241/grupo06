import React from 'react'
import Sidenav from '../../components/Sidenav'
import Navbar from '../../components/Navbar'
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import OrdConf1 from '../../components/confeccion/ordconf1';

export default function OrdenConfeccionPage() {
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
          Orden de producción
        </h3>
        
      <div><OrdConf1 /></div>
      </Box>

    </Box>
      
    
      
    </>
  )
}