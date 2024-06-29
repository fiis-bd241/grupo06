import React from "react";
import Sidenav from "../../components/Sidenav";
import Navbar from "../../components/Navbar";
import Box from "@mui/material/Box";
//navegation
import Navigation from "../../components/Navigation";
//import TablaCortesLotes from "../../components/corte/tablacortes";
import ProductionOrderTable from "../../components/corte/comp/numcortes";

export default function CortePage() {
  return (
    <>
      <Navbar />
      <Box height={30} />
      <Box sx={{ display: "flex" }}>
        <Sidenav />

        <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
          <h1>Área de Corte</h1>
          <div>
            <Navigation />
          </div>
          <h3>Número de cortes por el orden alfabético</h3>
          {/*<TablaCortesLotes />*/}
          <ProductionOrderTable/>
        </Box>
        
      </Box>
    </>
  );
}
