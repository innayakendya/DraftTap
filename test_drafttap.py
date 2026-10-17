# test_drafttap.py
"""
Tests for DraftTap module.
"""

import unittest
from drafttap import DraftTap

class TestDraftTap(unittest.TestCase):
    """Test cases for DraftTap class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftTap()
        self.assertIsInstance(instance, DraftTap)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftTap()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
