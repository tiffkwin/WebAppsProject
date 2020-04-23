#################
#### imports ####
#################
 
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

################
#### config ####
################
 
app = Flask(__name__, template_folder='../templates', static_folder='../static')
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webapps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from .models import Zodiac

db.create_all()

from .models.Zodiac import Zodiac

Zodiac.query.delete()

zodiacs = [
    Zodiac(zodiac_name="Sagittarius", 
    dates="11/22 - 12/21", 
    strengths="Generous, idealistic, great sense of humor.", 
    weaknesses="Promises more than can deliver, very impatient, will say anything no matter how undiplomatic.", 
    likes="Freedom, travel, philosophy, being outdoors.", 
    dislikes="Clingy people, being constrained, off-the-wall theories, details.", 
    description="""Curious and energetic, Sagittarius is one of the biggest travelers among all zodiac signs. Their open mind and philosophical view motivates them to wander around the world in search of the meaning of life. 
    Sagittarius is extrovert, optimistic and enthusiastic, and likes changes. Sagittarius-born are able to transform their thoughts into concrete actions and they will do anything to achieve their goals.
    Like the other fire signs, Sagittarius needs to be constantly in touch with the world to experience as much as possible. The ruling planet of Sagittarius is Jupiter, the largest planet of the zodiac. 
    Their enthusiasm has no bounds, and therefore people born under the Sagittarius sign possess a great sense of humor and an intense curiosity. Freedom is their greatest treasure, because only then they can freely travel and explore different cultures and philosophies. 
    Because of their honesty, Sagittarius-born are often impatient and tactless when they need to say or do something, so it's important to learn to express themselves in a tolerant and socially acceptable way."""),
    
    Zodiac(zodiac_name="Capricorn", 
    dates="12/22 - 1/19", 
    strengths="Responsible, disciplined, self-control, good managers.", 
    weaknesses="Know-it-all, unforgiving, condescending, expecting the worst.", 
    likes="Family, tradition, music, understated status, quality craftsmanship.", 
    dislikes="Almost everything at some point.", 
    description="""Capricorn is a sign that represents time and responsibility, and its representatives are traditional and often very serious by nature. These individuals possess an inner state of independence that enables significant progress both in their personal and professional lives. 
    They are masters of self-control and have the ability to lead the way, make solid and realistic plans, and manage many people who work for them at any time. They will learn from their mistakes and get to the top based solely on their experience and expertise. 
    Belonging to the element of Earth , like Taurus and Virgo, this is the last sign in the trio of practicality and grounding. Not only do they focus on the material world, but they have the ability to use the most out of it. Unfortunately, this element also makes them stiff and sometimes too stubborn to move from one perspective or point in a relationship. 
    They have a hard time accepting differences of other people that are too far from their character, and out of fear might try to impose their traditional values aggressively.
    Saturn is the ruling planet of Capricorn, and this planet represents restrictions of all kinds. Its influence makes these people practical and responsible, but also cold, distant and unforgiving, prone to the feeling of guilt and turned to the past. They need to learn to forgive in order to make their own life lighter and more positive.
    Capricorn – the Goat of Fear A goat with the tail of a fish is created to face fear and create panic. It is the sign of decisions made to be protected from monsters in our minds, lives, and immediate physical surrounding. 
    Always ready to transform into something that scares those scary things off, Capricorn speaks of each natural chain reaction of fear, where one scary thing leads to many others, rising up as defensive mechanisms that only make things worse. Immersed in their secrecy, they face the world just as they are – brave enough to never run away, but constantly afraid of their inner monsters."""),
    
    Zodiac(zodiac_name="Aquarius", 
    dates="1/20 - 2/18", 
    strengths="Progressive, original, independent, humanitarian.", 
    weaknesses="Runs from emotional expression, temperamental, uncompromising, aloof.", 
    likes="Fun with friends, helping others, fighting for causes, intellectual conversation, a good listener.", 
    dislikes="Limitations, broken promises, being lonely, dull or boring situations, people who disagree with them.", 
    description="""Aquarius-born are shy and quiet , but on the other hand they can be eccentric and energetic. However, in both cases, they are deep thinkers and highly intellectual people who love helping others. They are able to see without prejudice, on both sides, which makes them people who can easily solve problems.
    Although they can easily adapt to the energy that surrounds them, Aquarius-born have a deep need to be some time alone and away from everything, in order to restore power. People born under the Aquarius sign, look at the world as a place full of possibilities.
    Aquarius is an air sign, and as such, uses his mind at every opportunity. If there is no mental stimulation, they are bored and lack a motivation to achieve the best result.
    The ruling planet of Aquarius, Uranus has a timid, abrupt and sometimes aggressive nature, but it also gives Aquarius visionary quality. They are capable of perceiving the future and they know exactly what they want to be doing five or ten years from now.
    Uranus also gave them the power of quick and easy transformation, so they are known as thinkers, progressives and humanists. They feel good in a group or a community, so they constantly strive to be surrounded by other people.
    The biggest problem for Aquarius-born is the feeling that they are limited or constrained. Because of the desire for freedom and equality for all, they will always strive to ensure freedom of speech and movement. Aquarius-born have a reputation for being cold and insensitive persons, but this is just their defence mechanism against premature intimacy. They need to learn to trust others and express their emotions in a healthy way."""),

    Zodiac(zodiac_name="Pisces", 
    dates="2/19 - 3/20", 
    strengths="Compassionate, artistic, intuitive, gentle, wise, musical.", 
    weaknesses="Fearful, overly trusting, sad, desire to escape reality, can be a victim or a martyr.", 
    likes="Being alone, sleeping, music, romance, visual media, swimming, spiritual themes.", 
    dislikes="Know-it-all, being criticized, the past coming back to haunt, cruelty of any kind.", 
    description="""Pisces are very friendly, so they often find themselves in a company of very different people. Pisces are selfless, they are always willing to help others, without hoping to get anything back.
    Pisces is a Water sign and as such this zodiac sign is characterized by empathy and expressed emotional capacity.
    Their ruling planet is Neptune, so Pisces are more intuitive than others and have an artistic talent. Neptune is connected to music, so Pisces reveal music preferences in the earliest stages of life. They are generous, compassionate and extremely faithful and caring.
    People born under the Pisces sign have an intuitive understanding of the life cycle and thus achieve the best emotional relationship with other beings.
    Pisces-born are known by their wisdom, but under the influence of Uranus, Pisces sometimes can take the role of a martyr, in order to catch the attention. Pisces are never judgmental and always forgiving. They are also known to be most tolerant of all the zodiac signs."""),
    
    Zodiac(zodiac_name="Aries", 
    dates="3/21 - 4/19", 
    strengths="Courageous, determined, confident, enthusiastic, optimistic, honest, passionate.", 
    weaknesses="Impatient, moody, short-tempered, impulsive, aggressive.", 
    likes="Comfortable clothes, taking on leadership roles, physical challenges, individual sports.", 
    dislikes="Inactivity, delays, work that does not use one's talents.", 
    description="""As the first sign in the zodiac, the presence of Aries always marks the beginning of something energetic and turbulent. They are continuously looking for dynamic, speed and competition, always being the first in everything - from work to social gatherings. Thanks to its ruling planet Mars and the fact it belongs to the element of Fire (just like Leo and Sagittarius), Aries is one of the most active zodiac signs. It is in their nature to take action, sometimes before they think about it well.
    The Sun in such high dignity gives them excellent organizational skills, so you'll rarely meet an Aries who isn't capable of finishing several things at once, often before lunch break! Their challenges show when they get impatient, aggressive and vent anger pointing it to other people. Strong personalities born under this sign have a task to fight for their goals, embracing togetherness and teamwork through this incarnation.
    Aries rules the head and leads with the head, often literally walking head first, leaning forwards for speed and focus. Its representatives are naturally brave and rarely afraid of trial and risk. They possess youthful strength and energy, regardless of their age and quickly perform any given tasks.
    Aries - the Flying Ram Guided by the story of the Golden Fleece, an Aries is ready to be the hero of the day, fly away and carry many endangered, powerless people on their back. The power of the ram is carried on his back, for he is the gold itself, shiny and attractive to those ready for betrayal. The story of glory that isn't easy to carry is in these two horns, and if this animal doesn't get shorn, allowing change and giving someone a warm sweater, they won't have much to receive from the world. Each Aries has a task to share their position, power, gold, or physical strength with other people willingly, or the energy will be stopped in its natural flow, fear will take over, and the process of giving and receiving will hold balance at zero. """),
    
    Zodiac(zodiac_name="Taurus", 
    dates="4/20 - 5/20", 
    strengths="Reliable, patient, practical, devoted, responsible, stable.", 
    weaknesses="Stubborn, possessive, uncompromising.", 
    likes="Gardening, cooking, music, romance, high quality clothes, working with hands.", 
    dislikes="Sudden changes, complications, insecurity of any kind, synthetic fabrics.", 
    description="""Practical and well-grounded, Taurus is the sign that harvests the fruits of labor. They feel the need to always be surrounded by love and beauty, turned to the material world, hedonism, and physical pleasures. People born with their Sun in Taurus are sensual and tactile, considering touch and taste the most important of all senses. Stable and conservative, this is one of the most reliable signs of the zodiac, ready to endure and stick to their choices until they reach the point of personal satisfaction.
    Taurus is an Earth sign, just like Virgo and Capricorn, and has the ability to see things from a grounded, practical and realistic perspective. They find it easy to make money and stay on same projects for years, or until they are completed. What we often see as stubbornness can be interpreted as commitment, and their ability to complete tasks whatever it takes is uncanny. This makes them excellent employees, great long-term friends and partners, always being there for people they love. Earthly note makes them overprotective, conservative, or materialistic at times, with views of the world founded on their love of money and wealth.
    The ruler of Taurus is Venus, the planet of love, attraction, beauty, satisfaction, creativity and gratitude. This tender nature will make Taurus an excellent cook, gardener, lover, and artist. They are loyal and don't like sudden changes, criticism or the chase of guilt people are often prone to, being somewhat dependable on other people and emotions they seem to be unable to let go of. Still, no matter their potential emotional challenge, these individuals have the ability to bring a practical voice of reason in any chaotic and unhealthy situation.
    Taurus – the Wandering Bull Being the one who betrayed their best friend, goddess Hera herself, this is an unfortunate being that has to wander the Earth in order to find freedom. As if something was always poking them behind their back, reminding them of happiness that once was, stinging and pushing forwards, they close up in their own worlds, lonely and separated from their core. To find love, a Taurus has to travel the world, change perspective or make a shift in their entire belief system and their system of values. """),
    
    Zodiac(zodiac_name="Gemini", dates="5/21 - 6/20", 
    strengths="Gentle, affectionate, curious, adaptable, ability to learn quickly and exchange ideas.", 
    weaknesses="Nervous, inconsistent, indecisive.", 
    likes="Music, books, magazines, chats with nearly anyone, short trips around the town.", 
    dislikes="Being alone, being confined, repetition and routine.", 
    description="""Expressive and quick-witted, Gemini represents two different personalities in one and you will never be sure which one you will face. They are sociable, communicative and ready for fun, with a tendency to suddenly get serious, thoughtful and restless. They are fascinated with the world itself, extremely curious, with a constant feeling that there is not enough time to experience everything they want to see.
    The sign of Gemini belongs to the element of Air, accompanying Libra and Aquarius, and this connects it to all aspects of the mind. It is ruled by Mercury, the planet that represents communication, writing, and movement. People born under this Sun sign often have a feeling that their other half is missing, so they are forever seeking new friends, mentors, colleagues and people to talk to.
    Gemini's changeable and open mind makes them excellent artists, especially writers and journalists, and their skills and flexibility make them shine in trade, driving and team sports. This is a versatile, inquisitive, fun loving sign, born with a wish to experience everything there is out there, in the world. This makes their character inspiring, and never boring.
    Gemini - the Caring Twins There is so much childish innocence in the nature of Gemini, telling their tale of brotherhood, love between best friends and relatives who are entirely different by character, circumstances, physical appearance or upbringing. They are in this world to mend differences and make them feel right, ready to give their life for a brother or a friend."""),
    
    Zodiac(zodiac_name="Cancer", 
    dates="6/21 - 7/22", 
    strengths="Tenacious, highly imaginative, loyal, emotional, sympathetic, persuasive.", 
    weaknesses="Moody, pessimistic, suspicious, manipulative, insecure.", 
    likes="Art, home-based hobbies, relaxing near or in water, helping loved ones, a good meal with friends.", 
    dislikes="Strangers, any criticism of Mom, revealing of personal life.", 
    description="""Deeply intuitive and sentimental, Cancer can be one of the most challenging zodiac signs to get to know. They are very emotional and sensitive, and care deeply about matters of the family and their home. Cancer is sympathetic and attached to people they keep close. Those born with their Sun in Cancer are very loyal and able to empathize with other people's pain and suffering.
    The sign of Cancer belongs to the element of Water, just like Scorpio and Pisces. Guided by emotion and their heart, they could have a hard time blending into the world around them. Being ruled by the Moon, phases of the lunar cycle deepen their internal mysteries and create fleeting emotional patterns that are beyond their control. As children, they don't have enough coping and defensive mechanisms for the outer world, and have to be approached with care and understanding, for that is what they give in return.
    Lack of patience or even love will manifest through mood swings later in life, and even selfishness, self-pity or manipulation. They are quick to help others, just as they are quick to avoid conflict, and rarely benefit from close combat of any kind, always choosing to hit someone stronger, bigger, or more powerful than they imagined. When at peace with their life choices, Cancer representatives will be happy and content to be surrounded by a loving family and harmony in their home.
    Cancer - the Brave Crab Sent to this Earth by something they believe in, only to mess with someone bigger than they are, this isn't an animal aware of their strength. Patriotism can make them endanger their own wellbeing, fighting for someone else's cause, as if others can become their higher power. The Crab knows where they're going, but this is often in a wrong direction, at least until they learn their lessons and start relying solely on themselves."""),
    
    Zodiac(zodiac_name="Leo", 
    dates="7/23 - 8/22", 
    strengths="Creative, passionate, generous, warm-hearted, cheerful, humorous.", 
    weaknesses="Arrogant, stubborn, self-centered, lazy, inflexible.", 
    likes="Theater, taking holidays, being admired, expensive things, bright colors, fun with friends.", 
    dislikes="Being ignored, facing difficult reality, not being treated like a king or queen.", 
    description="""People born under the sign of Leo are natural born leaders. They are dramatic, creative, self-confident, dominant and extremely difficult to resist, able to achieve anything they want to in any area of life they commit to. There is a specific strength to a Leo and their "king of the jungle" status. Leo often has many friends for they are generous and loyal. Self-confident and attractive, this is a Sun sign capable of uniting different groups of people and leading them as one towards a shared cause, and their healthy sense of humor makes collaboration with other people even easier.
    Leo belongs to the element of Fire, just like Aries and Sagittarius. This makes them warmhearted, in love with life, trying to laugh and have a good time. Able to use their mind to solve even the most difficult problems, they will easily take initiative in resolving various complicated situations. Ruled by the Sun, Leo worships this fiery entity in the sky, quite literally as well as metaphorically. They are in search for self-awareness and in constant growth of ego. Aware of their desires and personality, they can easily ask for everything they need, but could just as easily unconsciously neglect the needs of other people in their chase for personal gain or status. When a Leo representative becomes too fond and attached to their achievements and the way other people see them, they become an easy target, ready to be taken down.
    Leo - the Lion in the Cave The story of the Lion always speaks of bravery. This is an animal fearless and impossible to challenge, hurt or destroy, their only weaknesses being fear and aggression towards those they confront. Living in a cave, a Lion always needs to have one, nesting and finding comfort in hard times. However, they should never stay there for long. With their head high, they have to face others with dignity and respect, never raising a voice, a hand, or a weapon, bravely walking through the forest they rule."""),
    
    Zodiac(zodiac_name="Virgo", 
    dates="8/23 - 9/22", 
    strengths="Loyal, analytical, kind, hardworking, practical.", 
    weaknesses="Shyness, worry, overly critical of self and others, all work and no play.", 
    likes="Animals, healthy food, books, nature, cleanliness.", 
    dislikes="Rudeness, asking for help, taking center stage.", 
    description="""Virgos are always paying attention to the smallest details and their deep sense of humanity makes them one of the most careful signs of the zodiac. Their methodical approach to life ensures that nothing is left to chance, and although they are often tender, their heart might be closed for the outer world. This is a sign often misunderstood, not because they lack the ability to express, but because they won’t accept their feelings as valid, true, or even relevant when opposed to reason. The symbolism behind the name speaks well of their nature, born with a feeling they are experiencing everything for the first time.
    Virgo is an Earth sign, fitting perfectly between Taurus and Capricorn. This will lead to a strong character, but one that prefers conservative, well-organized things and a lot of practicality in their everyday life. These individuals have an organized life, and even when they let go to chaos, their goals and dreams still have strictly defined borders in their mind. Constantly worried that they missed a detail that will be impossible to fix, they can get stuck in details, becoming overly critical and concerned about matters that nobody else seems to care much about.
    Since Mercury is the ruling planet of this sign, its representatives have a well-developed sense of speech and writing, as well as all other forms of communication. Many Virgos may choose to pursue a career as writers, journalists, and typists, but their need to serve others makes them feel good as caregivers, on a clear mission to help.
    Virgo – the Disappointed Goddess Seeking goodness in humankind is the story of Virgo, and disappointment seems to be inevitable from their point of view. The first time they came from their cloud and jumped onto planet Earth, it felt like their mission is to use their existence for good, discovering ways of justice and purity in other people. Once they fail to find it too many times, Virgos will pull away, get lost, turn to substance abuse, or simply separate from other people to sit on the bench, criticize and judge. """),
    
    Zodiac(zodiac_name="Libra", 
    dates="9/23 - 10/22", 
    strengths="Cooperative, diplomatic, gracious, fair-minded, social.", 
    weaknesses="Indecisive, avoids confrontations, will carry a grudge, self-pity.", 
    likes="Harmony, gentleness, sharing with others, the outdoors.", 
    dislikes="Violence, injustice, loudmouths, conformity.", 
    description="""People born under the sign of Libra are peaceful, fair, and they hate being alone. Partnership is very important for them, as their mirror and someone giving them the ability to be the mirror themselves. These individuals are fascinated by balance and symmetry, they are in a constant chase for justice and equality, realizing through life that the only thing that should be truly important to themselves in their own inner core of personality. This is someone ready to do nearly anything to avoid conflict, keeping the peace whenever possible
    The sign of Libra is an Air sign, set between Gemini and Aquarius, giving these individuals constant mental stimuli, strong intellect and a keen mind. They will be inspired by good books, insurmountable discussions and people who have a lot to say. Each Libra representative has to be careful when talking to other people, for when they are forced to decide about something that is coming their way, or to choose sides, they suddenly realize that they might be in the wrong place and surrounded by wrong people. No partner should make them forget that they have their own opinion.
    Planet ruling the sign of Libra is Venus, making these people great lovers but also fond of expensive, material things. Their lives need to be enriched by music, art, and beautiful places they get a chance to visit.
    Libra – The Measure of Our Souls The shortest myth of them all seems to present a good analogy to the shortest constellation in the sky, you might even say that it is non-existent, presented by the pliers of Scorpio. Libra is one dot of balance in the sea of different extremes, manifested only through the fifteenth degree of this magnificent sign, an object among animals and people. There is something awfully insecure about Libra, as if they were unsure which plate to burden next, aware that things pass and teach us to be careful around other people. Whatever we do in our lifetimes, only serves to point the way for our Souls towards that “higher power” to finally measure our existence. Telling us where we went wrong or what we did right, Libras unconsciously teach us that true liberation hides in lightness."""),
    
    Zodiac(zodiac_name="Scorpio", 
    dates="10/23 - 11/21", 
    strengths="Resourceful, brave, passionate, stubborn, a true friend.", 
    weaknesses="Distrusting, jealous, secretive, violent.", 
    likes="Truth, facts, being right, longtime friends, teasing, a grand passion.", 
    dislikes="Dishonesty, revealing secrets, passive people.", 
    description="""Scorpio-born are passionate and assertive people. They are determined and decisive, and will research until they find out the truth. Scorpio is a great leader, always aware of the situation and also features prominently in resourcefulness.
    Scorpio is a Water sign and lives to experience and express emotions. Although emotions are very important for Scorpio, they manifest them differently than other water signs. In any case, you can be sure that the Scorpio will keep your secrets, whatever they may be.
    Pluto is the planet of transformation and regeneration, and also the ruler of this zodiac sign. Scorpios are known by their calm and cool behavior, and by their mysterious appearance. People often say that Scorpio-born are fierce, probably because they understand very well the rules of the universe. Some Scorpio-born can look older than they actually are. They are excellent leaders because they are very dedicated to what they do. Scorpios hate dishonesty and they can be very jealous and suspicious, so they need to learn how to adapt more easily to different human behaviors. Scorpios are brave and therefore they have a lot of friends.""")]

db.session.bulk_save_objects(zodiacs)
db.session.commit()
 
####################
#### blueprints ####
####################
 
# from kfw-backend.services import file_blueprint
 
# register the blueprints
# app.register_blueprint(file_blueprint)