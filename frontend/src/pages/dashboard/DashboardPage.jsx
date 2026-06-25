import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { Package, FileText, AlertTriangle, TrendingUp } from 'lucide-react'
import { PieChart, Pie, Cell, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'
import api, { recuperateursAPI } from '../../api'
import { useAuthStore } from '../../store'

const COLORS = ['#4F46E5','#10b981','#f59e0b','#ef4444','#8b5cf6','#14b8a6','#6b7280']

const CLASSE_LABELS = {
  D:  'Déchets ordinaires',
  S:  'Déchets spéciaux',
  SD: 'Déchets spéciaux dangereux',
  MA: 'Ménagers et assimilés',
  '': 'Non classé',
}

const MOIS_LABELS = [
  'Jan','Fév','Mar','Avr','Mai','Juin','Juil','Août','Sep','Oct','Nov','Déc',
]

export default function DashboardPage() {
  const { user } = useAuthStore()
  const [tracaStats,   setTracaStats]   = useState(null)
  const [alerts,       setAlerts]       = useState([])

  const titre = user?.recuperateur_nom || 'Tableau de bord'
  const isRecup = user?.role === 'RECUPERATEUR'

  useEffect(() => {
    recuperateursAPI.alerts().then(r => setAlerts(r.data.alerts || [])).catch(() => {})
    const params = {}
    if (isRecup && user?.recuperateur_id) params.recuperateur = user.recuperateur_id
    api.get('/traceability/stats/', { params }).then(r => setTracaStats(r.data)).catch(() => {})
  }, [])

  const evolution = (tracaStats?.evolution || []).map(e => {
    const [y, m] = e.mois.split('-')
    return { ...e, label: `${MOIS_LABELS[Number(m) - 1] || m} ${y}` }
  })
  const parClasse = (tracaStats?.par_classe || []).map(c => ({
    ...c,
    label: CLASSE_LABELS[c.classe_dechet] || c.classe_dechet || 'Non classé',
  }))

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-bold text-slate-900 dark:text-white">{titre}</h1>
        <p className="text-slate-500 text-sm mt-0.5">Système de gestion des récupérateurs de déchets — Algérie</p>
      </div>

      {/* Alerts banner */}
      {alerts.length > 0 && (
        <div className="card border-l-4 border-red-500 bg-red-50/40 p-4 flex items-start gap-3">
          <AlertTriangle size={18} className="text-red-500 flex-shrink-0 mt-0.5" />
          <div>
            <p className="font-semibold text-red-800 text-sm">{alerts.length} alerte(s) active(s)</p>
            <p className="text-xs text-red-600 mt-0.5">{alerts[0]?.message}</p>
          </div>
        </div>
      )}

      {/* Charts */}
      {tracaStats && (
        <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">
          {/* Évolution des déchets récupérés */}
          <div className="card p-5">
            <h3 className="font-bold text-slate-900 dark:text-white mb-4 flex items-center gap-2">
              <TrendingUp size={16} className="text-primary-600" /> Évolution des déchets récupérés
            </h3>
            {evolution.length === 0 ? (
              <p className="text-sm text-slate-400 text-center py-12">Aucune donnée pour le moment</p>
            ) : (
              <ResponsiveContainer width="100%" height={220}>
                <LineChart data={evolution} margin={{ left: -10, bottom: 5 }}>
                  <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f1f5f9" />
                  <XAxis dataKey="label" tick={{ fontSize: 10 }} />
                  <YAxis tick={{ fontSize: 10 }} />
                  <Tooltip formatter={(v) => [`${v} kg`, 'Quantité']} />
                  <Line type="monotone" dataKey="quantite" name="Quantité récupérée"
                    stroke="#4F46E5" strokeWidth={2} dot={{ r: 3 }} />
                </LineChart>
              </ResponsiveContainer>
            )}
          </div>

          {/* Catégories / types de déchets récupérés */}
          <div className="card p-5">
            <h3 className="font-bold text-slate-900 dark:text-white mb-4 flex items-center gap-2">
              <Package size={16} className="text-primary-600" /> Types de déchets récupérés
            </h3>
            {parClasse.length === 0 ? (
              <p className="text-sm text-slate-400 text-center py-12">Aucune donnée pour le moment</p>
            ) : (
              <div className="flex gap-4 items-center">
                <ResponsiveContainer width="50%" height={180}>
                  <PieChart>
                    <Pie data={parClasse} dataKey="count" cx="50%" cy="50%" outerRadius={70}
                      label={({ percent }) => `${(percent*100).toFixed(0)}%`} labelLine={false}>
                      {parClasse.map((_,i) => <Cell key={i} fill={COLORS[i%COLORS.length]} />)}
                    </Pie>
                    <Tooltip formatter={(v,n,p) => [v, p.payload.label]} />
                  </PieChart>
                </ResponsiveContainer>
                <div className="flex-1 space-y-2">
                  {parClasse.map((r, i) => (
                    <div key={r.classe_dechet || i} className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <div className="w-3 h-3 rounded-full" style={{ background: COLORS[i%COLORS.length] }} />
                        <span className="text-xs text-slate-600">{r.label}</span>
                      </div>
                      <span className="text-xs font-bold">{r.count}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Quick links */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
        {[
          { to: '/tracabilite',       label: 'Nouveau dossier',      icon: Package, color: 'border-emerald-200 hover:border-emerald-400 hover:bg-emerald-50' },
          { to: '/documents',         label: 'BSD / Déclarations',   icon: FileText, color: 'border-amber-200 hover:border-amber-400 hover:bg-amber-50' },
        ].map(item => (
          <Link key={item.label} to={item.to}
            className={`card p-4 flex items-center gap-3 border-2 transition-all ${item.color}`}>
            <item.icon size={18} className="text-slate-600 flex-shrink-0" />
            <span className="text-sm font-semibold text-slate-700 leading-tight">{item.label}</span>
          </Link>
        ))}
      </div>
    </div>
  )
}
