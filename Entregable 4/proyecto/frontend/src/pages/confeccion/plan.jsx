import React from 'react'
import Sidenav from '../../components/Sidenav'
import Navbar from '../../components/Navbar'
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import OrdAsig1 from '../../components/confeccion/ordasig1';

export default function PlanPage() {
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
        
      <div><OrdAsig1 /></div>
      </Box>

    </Box>
      
    
      
    </>
  )
}