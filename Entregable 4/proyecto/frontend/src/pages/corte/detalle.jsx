import React from 'react'
import Sidenav from '../../components/Sidenav'
import Navbar from '../../components/Navbar'
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
//navegation
import Navigation from "../../components/Navigation";

export default function DetallePage() {
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
        <Typography paragraph>
          resumen
        </Typography>
      </Box>

    </Box>
      
    
      
    </>
  )
}