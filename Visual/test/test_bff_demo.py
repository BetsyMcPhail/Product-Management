#---------------------------------------------------------------------------
# Copyright 2015 The Open Source Electronic Health Record Alliance
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#---------------------------------------------------------------------------
from selenium import webdriver
import argparse
import unittest
import time

class test_bff(unittest.TestCase):

  @classmethod
  def tearDownClass(cls):
    global driver
    driver.close()

  def test_01_expand_collapse_nodes(self):
    global driver
    time.sleep(5)
    nodes = driver.find_elements_by_class_name('node')
    # Page opens with some nodes expanded
    oldSize = len(nodes)
    # Click on root node to collapse all nodes"
    try:
        nodes[-1].find_element_by_tag_name("path").click()
    except:
        nodes[-1].find_element_by_tag_name("path").click()
    # Now, only the root node should be visible
    time.sleep(1)
    nodes = driver.find_elements_by_class_name('node')
    self.assertNotEqual(len(nodes), oldSize)
    self.assertEqual(len(nodes), 1)
    # Click on root node again
    nodes[-1].find_element_by_tag_name("path").click()
    time.sleep(1)
    # Should be back where we started
    nodes = driver.find_elements_by_class_name('node')
    self.assertEqual(len(nodes), oldSize)

  def test_02_collapse_all(self):
    global driver
    oldSize = len(driver.find_elements_by_class_name('node'))
    button = driver.find_element_by_xpath("//button[contains(@onclick,'_collapseAllNode')]")
    button.click()
    time.sleep(1)
    newSize = len(driver.find_elements_by_class_name('node'))
    self.assertTrue(oldSize > newSize)
    self.assertEqual(newSize, 1)

  def test_03_reset(self):
    global driver
    oldSize = len(driver.find_elements_by_class_name('node'))
    button = driver.find_element_by_xpath("//button[contains(@onclick,'_collapseAllNode')]")
    button.click()
    time.sleep(1)
    button = driver.find_element_by_xpath("//button[contains(@onclick,'_resetAllNode')]")
    button.click()
    time.sleep(1)
    newSize = len(driver.find_elements_by_class_name('node'))
    self.assertTrue(oldSize < newSize)

  def test_04_click_filter(self):
    global driver
    time.sleep(5)
    oldSize = len(driver.find_elements_by_class_name('node'))
    filterBox = driver.find_element_by_id("showUpdates")
    filterBox.click()
    time.sleep(1)
    newSize = len(driver.find_elements_by_class_name('node'))
    self.assertTrue(oldSize > newSize)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="")
  parser.add_argument("-r",dest = 'webroot', required=True, help="Web root of the ViViaN(TM) instance to test.  eg. http://code.osehra.org/vivian/")
  result = vars(parser.parse_args())
  driver = webdriver.Firefox()
  driver.get(result['webroot'] + "/bff_demo.php")
  suite = unittest.TestLoader().loadTestsFromTestCase(test_bff)
  unittest.TextTestRunner(verbosity=2).run(suite)