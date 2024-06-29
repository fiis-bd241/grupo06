import React from 'react'
import {Routes, Route, HashRouter} from "react-router-dom"
import Home from "./pages/Home"
import A1 from "./pages/A1"
import A2 from "./pages/A2"
import A3 from "./pages/A3"
import A4 from "./pages/A4"
import A5 from "./pages/A5"
import A6 from "./pages/A6"
import A7 from "./pages/A7"

// Acabados
import AcabadoPage from './pages/acabados/acabados';
import LotesPage from './pages/acabados/lotes';
import Reporte from './pages/acabados/reporte';
import Detalle from './pages/acabados/detalle';
import CajaOp from './pages/acabados/caja-operario';



// Almacén Central
import SolicitudPage from './pages/almacencentral/solicitud';
import EstadoInvPage from './pages/almacencentral/estado-inv';
import EstadoPage from './pages/almacencentral/estado';
import ResumenPage from './pages/almacencentral/resumen';


// Calidad
import Tipo1Page from './pages/calidad/tipo-1';
import Tipo2Page from './pages/calidad/tipo-2';
import Tipo3Page from './pages/calidad/tipo-3';

// Confección
import GuiaPage from './pages/confeccion/guia';
import OrdenConfeccionPage from './pages/confeccion/orden';
import PlanPage from './pages/confeccion/plan';

// Corte
import OrdenCortePage from './pages/corte/orden';
import OperarioCortePage from './pages/corte/operario';
import ActividadesPage from './pages/corte/actividades';
import CorteLotePage from './pages/corte/corte-lote';
import DetallePage from './pages/corte/detalle';
import ActividadesMaquinaPage from './pages/corte/actividadesmaquina';
import LotesCortePage from './pages/corte/lotes';
import CortesPage from './pages/corte/corte';

// PCP
import ControlarPage from './pages/pcp/controlar';
import EstadoPage1 from './pages/pcp/estado';
import ProgramarPage from './pages/pcp/programar';

// Tránsito
import Transito1Page from './pages/transito/1';
import Transito2Page from './pages/transito/2';
import Transito3Page from './pages/transito/3';
import CajaPrendaDetail from './components/acabados/CajaPrendaDetail'



export default function App() {
  return (
    <>
      <HashRouter>
        <Routes>
          <Route path="/" exact element={<Home />}></Route>
          <Route path="/almacencentral" exact element={<A1 />}></Route>
          <Route path="/corte" exact element={<A2 />}></Route>
          <Route path="/confeccion" exact element={<A3 />}></Route>
          <Route path="/transito" exact element={<A4 />}></Route>
          <Route path="/acabados" exact element={<A5 />}></Route>
          <Route path="/calidad" exact element={<A6 />}></Route>
          <Route path="/pcp" exact element={<A7 />}></Route>


          {/* Acabados */}
          <Route path="/acabados/acabados" element={<AcabadoPage />} />
          <Route path="/acabados/lotes" element={<LotesPage />} />
          <Route path="/cajas/:id_caja" element={<CajaPrendaDetail />} />
          <Route path="/acabados/lotes/reporte" element={<Reporte />} />
          <Route path="/acabados/lotes/detalle" element={<Detalle />} />
          <Route path="/acabados/acabados/caja-operario" element={<CajaOp />} />

          {/* Almacén Central */}
          <Route path="/almacencentral/solicitud" element={<SolicitudPage />} />
          <Route path="/almacencentral/estado-inv" element={<EstadoInvPage />} />
          <Route path="/almacencentral/estado" element={<EstadoPage />} />
          <Route path="/almacencentral/resumen" element={<ResumenPage />} />
        
        {/* Calidad */}
        <Route path="/calidad/tipo-1" element={<Tipo1Page />} />
        <Route path="/calidad/tipo-2" element={<Tipo2Page />} />
        <Route path="/calidad/tipo-3" element={<Tipo3Page />} />

        {/* Confección */}
        <Route path="/confeccion/guia" element={<GuiaPage />} />
        <Route path="/confeccion/orden" element={<OrdenConfeccionPage />} />
        <Route path="/confeccion/plan" element={<PlanPage />} />
        
        {/* Corte */}
        <Route path="/corte/operario" element={<OperarioCortePage />} />
        <Route path="/corte/operario/actividades" element={<ActividadesPage />} />
        <Route path="/corte/operario/corte-lote" element={<CorteLotePage />} />
        <Route path="/corte/orden" element={<OrdenCortePage />} />
        <Route path="/corte/detalle" element={<DetallePage />} />
        <Route path="/corte/detalle/actividadesmaquina" element={<ActividadesMaquinaPage />} />
        <Route path="/corte/detalle/lotes" element={<LotesCortePage />} />
        <Route path="/corte/detalle/corte" element={<CortesPage />} />
        
        {/* PCP */}
        <Route path="/pcp/controlar" element={<ControlarPage />} />
        <Route path="/pcp/estado" element={<EstadoPage1 />} />
        <Route path="/pcp/programar" element={<ProgramarPage />} />
        
        {/* Tránsito */}
        <Route path="/transito/1" element={<Transito1Page />} />
        <Route path="/transito/2" element={<Transito2Page />} />
        <Route path="/transito/3" element={<Transito3Page />} />

        </Routes>
      </HashRouter>
    </>
  )
}
