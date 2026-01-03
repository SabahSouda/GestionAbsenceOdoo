from odoo import models, fields

class AbsenceProfesseur(models.Model):
    _name = 'absence.professeur'
    _description = 'Absence des Professeurs'

    professeur_id = fields.Many2one('absence.professeur.master', string="Professeur", required=True)
    matiere = fields.Char(related='professeur_id.matiere', string="Matière", readonly=True, store=True)
    date_absence = fields.Date(string="Date d'absence", required=True, default=fields.Date.context_today)
    motif = fields.Text(string="Motif")
    etat = fields.Selection([
        ('en_attente', 'En attente'),
        ('valide', 'Validée'),
        ('refuse', 'Refusée')
    ], string="État", default='en_attente')

    user_id = fields.Many2one('res.users', string="Créé par", default=lambda self: self.env.user)

    def action_save_and_back(self):
        """Saves the record and returns to the dashboard."""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Accueil',
            'res_model': 'absence.dashboard',
            'view_mode': 'form',
            'target': 'current',
        }

    def action_valider(self):
        self.write({'etat': 'valide'})

    def action_refuser(self):
        self.write({'etat': 'refuse'})
