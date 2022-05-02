from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_homepage(self):
    
        with self.client:
            response = self.client.get('/root/index')
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            self.assertIn(b'<p>High Score: </p>', response.data)
            self.assertIn(b'<p>Score: </p>', response.data)
            self.assertIn(b'<p> Time Left: </p>', response.data)

    def test_valid_word(self):

        with self.client as client:
            with client.session_transaction() as session:
                session['board'] = [["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"]]
        response = self.client.get('/check-word?word=cat')
        self.assertEqual(response.json['result'], 'ok')

    def test_invalid_word(self):

        self.client.get('/root')
        response = self.client.get('/check-word?word=impossible')
        self.assertEqual(response.json['result'],'not-on-board')
