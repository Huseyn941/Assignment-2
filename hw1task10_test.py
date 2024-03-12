import Task_10
from random import choice, randint
import unittest
from unittest.mock import patch
from io import StringIO

class TestMainFunction(unittest.TestCase):

  def test_input_vowel(self):
        input_value = [(-1.9758556722906713, 4.7411615995688114, False), (-2.2562193679285074, 3.5737878430374654, False), (-1.6594531691233687, 3.634399143298819, True), (-2.52926788608845, 2.6573078408998, False), (-0.6527975800009851, 3.5099479728695337, True), (-0.09538482883016508, 4.320711152902637, False), (-2.076084956826957, 5.1243144086416095, False), (-0.4198373372982549, 4.100553069800245, False), (-2.488917389515537, 5.237240144025386, True), (-2.6552419003569914, 0.8850564160685745, False), (-0.8882972576869639, 5.744972898860526, False), (-0.09509956672527586, 5.620903316233118, False), (-0.7652897869137081, 4.373571224148183, False), (-2.7826790800095704, 4.158259254503808, False), (-2.9090480327442316, 3.0750268723386585, False), (-2.3373876955886637, 4.698795600286861, True), (-2.915222789977461, 4.3206967656421424, False), (-0.3975011002784523, 1.0040101670428097, True), (-0.9528221911608696, 1.3466845111416517, True), (-0.49347960494089893, 2.567292067862205, True), (-1.5025752797387248, 5.186414069461813, False), (-0.5094725311243224, 0.7531192701977958, True), (-2.578117971712711, 4.56800498550501, False), (-2.1404435482798747, 4.89262478604988, False), (-0.6487528366092028, 0.314557318278746, True), (0.6297498073868231, -0.20490383543195279, True), (1.1624701795400574, 9.316074585264166, True), (1.6722328545668261, 5.520587735978773, True), (0.01311115083192571, 2.0678038059420936, True), (1.4911563740208689, 5.2280062835772005, True), (0.5936220796226932, 2.1857502910462596, True), (0.949862527101228, 8.57791678453319, True), (1.6683180978580767, 8.553977821330989, True), (1.2432784938634676, 2.8845896883518964, True), (0.6872857833574673, 4.467777616422789, True), (1.2798630906342439, 8.918748067632821, True), (1.494768728978118, 1.7573195502721477, True), (1.2615415173230649, 2.1204624938852197, True), (1.2652303240801064, 3.240261241446103, True), (0.9519226140619446, 4.116128671058256, True), (1.0287655671250804, 2.6843171014588965, True), (0.49586231092877875, 5.792457764689441, True), (0.5305271418302697, 6.115569071490551, True), (0.7050797434112526, 6.407500939336269, True), (0.5076102196824737, 4.640461742789764, True), (0.7451494079293273, 8.721075642565847, True), (1.3922282892287299, 7.660312084415422, True), (0.9015986239766436, 9.603237998283205, True), (1.3923313221912657, 6.6218875110517885, True), (1.4808420714784774, 6.76512686087486, True), (-1.3846879468136448, -4.38417375604711, True), (0.9932732195068412, 0.4745752744284156, True), (0.6361107200904761, 0.692293701698882, True), (-0.9838589706307037, 0.7529784753952662, True), (-0.1438376290435941, 0.670052307712047, True), (-0.9433774799411121, 0.9476324835429583, True), (0.7885077136183749, 0.9092918489357698, True), (0.19693531587486457, 0.1821739387241469, True), (0.5914779337561764, 0.04174580934291727, True), (-0.6218487630138907, 0.2602097008043154, True), (-0.4627616222129336, 0.492265793225396, True), (-0.167650464588188, 0.7435014978053524, True), (0.12769935215590755, 0.6723160647331755, True), (-0.08967737608806092, 0.5999202708549871, True), (0.49196994394055205, 0.6473459512342999, True), (-0.9083435981017811, 0.8628610548714649, True), (-0.1502047786096019, 0.8323213395806077, True), (0.7797537851790823, 0.801776009591201, True), (-0.3092012300040796, 0.9370685769742814, True), (0.981084427080265, 0.9350929108679448, True), (-0.7881393971564787, 0.9109624386733048, True), (-0.19040922436786123, 0.1180741918249879, True), (0.6364922172777336, 0.21813286146503197, True), (0.3014247079938426, 0.3214068193832108, True), (0.3945019551410638, 0.33763596638267324, True), (-0.3333884870446626, 1.3861887001725108, True), (1.1471338389695553, -1.2065658363771696, True), (-1.1792021798688355, 0.5029307786735542, True), (-1.453653742883128, -2.8349793240325383, True), (-0.8757887580937305, -0.07748198489887859, True), (-1.312569242428133, -1.626295456052676, True), (0.47113779686047463, -2.399430533692589, True), (-0.9589970905321841, -1.8762385059131685, True), (-0.48363979324190787, -3.12958333915671, True), (1.7500117145783927, -0.2548640607862289, True), (1.0664066874353462, -3.7983492306708597, True), (-0.7301012663604394, -4.874062705069285, True), (1.605965799380693, -3.348677884354176, True), (-1.6721045355103694, -3.2183110900315826, True), (-0.06816821893443237, -3.584134753078512, True), (0.5584037991899344, 1.4202458071246715, True), (1.427151752426545, 0.7231511556932801, True), (-0.8383064600270629, -1.3434472526808552, True), (1.4975702876083612, -2.7857550019830386, True), (-1.5787862590771105, -2.9345271318382697, True), (-1.2663491473684405, -2.3097361693795513, True), (1.5893424745619251, -1.4204181800113305, True), (-1.3423597349684253, -2.4492839923621292, True), (0.17561873747893575, -2.1296801806307037, True), (0.8923160351997863, -0.5179727897393418, True)]
        expected_output = ("The point is not in the shaded area", "The point is in the shaded area")
        
        for _ in range(randint(10,30)):
            test = choice(input_value)
            with patch('builtins.input', side_effect=test[:2]), \
                patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                Task_10.main()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output[test[2]])

if __name__ == '__main__':
    unittest.main()
