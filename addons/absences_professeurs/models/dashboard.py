from odoo import models, fields, api

class AbsenceDashboard(models.TransientModel):
    _name = 'absence.dashboard'
    _description = 'Dashboard de gestion des absences'

    count_total = fields.Integer(string="Total")
    count_pending = fields.Integer(string="En attente")
    count_validated = fields.Integer(string="Validées")
    count_refused = fields.Integer(string="Refusées")
    absence_ids = fields.Many2many('absence.professeur', string="Absences")
    professeur_master_ids = fields.Many2many('absence.professeur.master', string="Professeurs Masters")

    @api.model
    def default_get(self, fields_list):
        res = super(AbsenceDashboard, self).default_get(fields_list)
        absences = self.env['absence.professeur'].sudo().search([])
        professeurs = self.env['absence.professeur.master'].sudo().search([])
        res.update({
            'count_total': len(absences),
            'count_pending': len(absences.filtered(lambda a: a.etat == 'en_attente')),
            'count_validated': len(absences.filtered(lambda a: a.etat == 'valide')),
            'count_refused': len(absences.filtered(lambda a: a.etat == 'refuse')),
            'absence_ids': [(6, 0, absences.ids)],
            'professeur_master_ids': [(6, 0, professeurs.ids)],
        })
        return res

    def action_open_liste_professeurs(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Gestion des Professeurs',
            'res_model': 'absence.dashboard',
            'view_mode': 'form',
            'views': [(self.env.ref('absences_professeurs.view_absence_dashboard_prof_manager').id, 'form')],
            'target': 'current',
        }

    def action_open_professeur(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Déclarer mon Absence',
            'res_model': 'absence.professeur',
            'view_mode': 'form',
            'view_id': self.env.ref('absences_professeurs.view_absence_form_prof').id,
            'target': 'current',
            'context': {'form_view_initial_mode': 'edit'}, # Ouvre directement en saisie
        }

    def action_open_responsable(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Espace Responsable (Tableau de Bord)',
            'res_model': 'absence.dashboard',
            'view_mode': 'form',
            'views': [(self.env.ref('absences_professeurs.view_absence_dashboard_respo').id, 'form')],
            'target': 'current',
        }
