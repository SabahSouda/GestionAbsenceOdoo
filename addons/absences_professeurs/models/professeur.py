from odoo import models, fields, api

class AbsenceProfesseurMaster(models.Model):
    _name = 'absence.professeur.master'
    _description = 'Liste des Professeurs et Matières'

    name = fields.Char(string="Nom du Professeur", required=True)
    matiere = fields.Char(string="Matière", required=True)
    absence_ids = fields.One2many('absence.professeur', 'professeur_id', string="Absences")
    absence_count = fields.Integer(string="Nombre d'absences", compute="_compute_absence_count", store=True)

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Le nom du professeur doit être unique !')
    ]

    @api.depends('absence_ids')
    def _compute_absence_count(self):
        for record in self:
            record.absence_count = len(record.absence_ids)

    def action_back_to_dashboard(self):
        """Returns to the Responsable Dashboard."""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Espace Responsable',
            'res_model': 'absence.dashboard',
            'view_mode': 'form',
            'views': [(self.env.ref('absences_professeurs.view_absence_dashboard_respo').id, 'form')],
            'target': 'current',
        }
