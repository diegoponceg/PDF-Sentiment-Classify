import argparse
import io
import json
import os

from google.cloud import language
import numpy
import six


def classify(text, verbose=True):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Put the file path here" # You won't have to set it each time now
    
    """Classify the input text into categories. """

    language_client = language.LanguageServiceClient()

    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)
    response = language_client.classify_text(document)
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            print(u'=' * 20)
            print(u'{:<16}: {}'.format('category', category.name))
            print(u'{:<16}: {}'.format('confidence', category.confidence))

    return result
classify(''' Anita Hill 

Opening Statement to the Senate Judiciary Committee 

Delivered 11 October 1991 

AUTHENTICITY CERTIFIED: Text version below transcribed directly from audio 

Note: Contains adult language and subject matter 

Ms. Hill: Mr. Chairman, Senator Thurmond, members of the committee: 

My name is Anita F. Hill, and I am a professor of law at the University of Oklahoma. I was 
born on a farm in Okmulgee County, Oklahoma, in 1956. I am the youngest of 13 children. I 
had my early education in Okmulgee County. My father, Albert Hill, is a farmer in that area. 
My mother's name is Irma Hill. She is also a farmer and a housewife. 

My childhood was one of a lot of hard work and not much money, but it was one of solid 
family affection, as represented by my parents. I was reared in a religious atmosphere in the 
Baptist faith, and I have been a member of the Antioch Baptist Church in Tulsa, Oklahoma, 
since 1983. It is a very warm part of my life at the present time. 

For my undergraduate work, I went to Oklahoma State University and graduated from there in 
1977. I am attaching to this statement a copy of my resume for further details of my 
education. 

Senator Biden: It will be included in the record as if read. 

Ms. Hill: Thank you. I graduated from the University with academic honors and proceeded to 
the Yale Law School, where I received my JD degree in 1980. Upon graduation from law 
school, I became a practicing lawyer with the Washington, DC, firm of Ward, Hardraker, and 
Ross.

Transcription by Michael E. Eidenmuller.  Property of AmericanRhetoric.com.  © Copyright 2008. All rights reserved.  Page 1 


AmericanRhetoric.com 

In 1981, I was introduced to now Judge Thomas by a mutual friend. Judge Thomas told me 
that he was anticipating a political appointment, and he asked if I would be interested in 
working with him. He was, in fact, appointed as Assistant Secretary of Education for Civil 
Rights. After he had taken that post, he asked if I would become his assistant, and I accepted 
that position. 

In my early period there, I had two major projects. The first was an article I wrote for Judge 
Thomas's signature on the education of minority students. The second was the organization of 
a seminar on high­risk students which was abandoned because Judge Thomas transferred to 
the EEOC where he became the chairman of that office. 

During this period at the Department of Education, my working relationship with Judge 
Thomas was positive. I had a good deal of responsibility and independence. I thought he 
respected my work and that he trusted my judgment. After approximately three months of 
working there, he asked me to go out socially with him. 

What happened next and telling the world about it are the two most difficult experiences of 
my life. It is only after a great deal of agonizing consideration and a great number of sleepless 
nights that I am able to talk of these unpleasant matters to anyone but my close friends. 

I declined the invitation to go out socially with him and explained to him that I thought it 
would jeopardize at what at the time I considered to be a very good working relationship. I 
had a normal social life with other men outside of the office. I believed then, as now, that 
having a social relationship with a person who was supervising my work would be ill­advised. I 
was very uncomfortable with the idea and told him so. 

I thought that by saying no and explaining my reasons my employer would abandon his social 
suggestions. However, to my regret, in the following few weeks, he continued to ask me out 
on several occasions. He pressed me to justify my reasons for saying no to him. These 
incidents took place in his office or mine. They were in the form of private conversations which 
would not have been overheard by anyone else. 

My working relationship became even more strained when Judge Thomas began to use work 
situations to discuss sex. On these occasions, he would call me into his office for reports on 
education issues and projects, or he might suggest that, because of the time pressures of his 
schedule, we go to lunch to a government cafeteria. After a brief discussion of work, he would 
turn the conversation to a discussion of sexual matters. 

His conversations were very vivid. He spoke about acts that he had seen in pornographic films 
involving such matters as women having sex with animals and films showing group sex or 
rape scenes. He talked about pornographic materials depicting individuals with large penises 
or large breasts involved in various sex acts. On several occasions, Thomas told me 
graphically of his own sexual prowess.

Transcription by Michael E. Eidenmuller.  Property of AmericanRhetoric.com.  © Copyright 2008. All rights reserved.  Page 2 


AmericanRhetoric.com 

Because I was extremely uncomfortable talking about sex with him at all, and particularly in 
such a graphic way, I told him that I did not want to talk about these subjects. I would also 
try to change the subject to education matters or to nonsexual personal matters such as his 
background or his beliefs. My efforts to change the subject were rarely successful. 

Throughout the period of these conversations, he also, from time to time, asked me for social 
engagements. My reaction to these conversations was to avoid them by eliminating 
opportunities for us to engage in extended conversations. This was difficult because at the 
time I was his only assistant at the Office of Education ­­ or Office for Civil Rights. 

During the latter part of my time at the Department of Education, the social pressures and 
any conversation of his offensive behavior ended. I began both to believe and hope that our 
working relationship could be a proper, cordial, and professional one. 

When Judge Thomas was made chair of the EEOC, I needed to face the question of whether to 
go with him. I was asked to do so, and I did. The work itself was interesting, and at that time 
it appeared that the sexual overtures which had so troubled me had ended. I also faced the 
realistic fact that I had no alternative job. While I might have gone back to private practice, 
perhaps in my old firm or at another, I was dedicated to civil rights work, and my first choice 
was to be in that field. Moreover, the Department of Education itself was a dubious venture. 
President Reagan was seeking to abolish the entire department. 

For my first months at the EEOC, where I continued to be an assistant to Judge Thomas, there 
were no sexual conversations or overtures. However, during the fall and winter of 1982, these 
began again. The comments were random and ranged from pressing me about why I didn't go 
out with him to remarks about my personal appearance. I remember his saying that some day 
I would have to tell him the real reason that I wouldn't go out with him. 

He began to show displeasure in his tone and voice and his demeanor and his continued 
pressure for an explanation. He commented on what I was wearing in terms of whether it 
made me more or less sexually attractive. The incidents occurred in his inner office at the 
EEOC. 

One of the oddest episodes I remember was an occasion in which Thomas was drinking a 
Coke in his office. He got up from the table at which we were working, went over to his desk 
to get the Coke, looked at the can and asked, "Who has pubic hair on my Coke?" On other 
occasions, he referred to the size of his own penis as being larger than normal, and he also 
spoke on some occasions of the pleasures he had given to women with oral sex. 

At this point, late 1982, I began to feel severe stress on the job. I began to be concerned that 
Clarence Thomas might take out his anger with me by degrading me or not giving me 
important assignments. I also thought that he might find an excuse for dismissing me.

Transcription by Michael E. Eidenmuller.  Property of AmericanRhetoric.com.  © Copyright 2008. All rights reserved.  Page 3 


AmericanRhetoric.com 

In January of 1983, I began looking for another job. I was handicapped because I feared that, 
if he found out, he might make it difficult for me to find other employment and I might be 
dismissed from the job I had. Another factor that made my search more difficult was that 
there was a period ­­ this was during a period of a hiring freeze in the government. In 
February 1983, I was hospitalized for five days on an emergency basis for an acute ­­ for 
acute stomach pain, which I attributed to stress on the job. 

Once out of the hospital, I became more committed to find other employment and sought 
further to minimize my contact with Thomas. This became easier when Allison Duncan 
became office director, because most of my work was then funneled through her and I had 
contact with Clarence Thomas mostly in staff meetings. 

In the spring of 1983, an opportunity to teach at Oral Roberts University opened up. I taught 
an afternoon session and seminar at Oral Roberts University. The dean of the university saw 
me teaching and inquired as to whether I would be interested in pursuing a career in teaching, 
beginning at Oral Roberts University. I agreed to take the job in large part because of my 
desire to escape the pressures I felt at the EEOC, due to Judge Thomas. 

When I informed him that I was leaving in July, I recall that his response was that now I 
would no longer have an excuse for not going out with him. I told him that I still preferred not 
to do so. At some time after that meeting, he asked if he could take me to dinner at the end 
of the term. When I declined, he assured me that the dinner was a professional courtesy only 
and not a social invitation. I reluctantly agreed to accept that invitation, but only if it was at 
the very end of a working day. 

On, as I recall, the last day of my employment at the EEOC in the summer of 1983, I did have 
dinner with Clarence Thomas. We went directly from work to a restaurant near the office. We 
talked about the work I had done, both at Education and at the EEOC. He told me that he was 
pleased with all of it except for an article and speech that I had done for him while we were at 
the Office for Civil Rights. Finally, he made a comment that I will vividly remember. He said 
that if I ever told anyone of his behavior that it would ruin his career. This was not an 
apology, nor was it an explanation. That was his last remark about the possibility of our going 
out or reference to his behavior. 

In July of 1983, I left Washington, D.C. area and I've had minimal contacts with Judge 
Clarence Thomas since. I am of course aware from the Press that some questions have been 
raised about conversations I had with Judge Clarence Thomas after I left the EEOC. From 
1983 until today, I have seen Judge Thomas only twice. On one occasion, I needed to get a 
reference from him, and on another he made a public appearance in Tulsa. 

On one occasion he called me at home and we had an inconsequential conversation. On one 
occasion he called me without reaching me, and I returned the call without reaching him, and 
nothing came of it. I have, on at least three occasions, been asked to [act] as a conduit to 
him for others.

Transcription by Michael E. Eidenmuller.  Property of AmericanRhetoric.com.  © Copyright 2008. All rights reserved.  Page 4 


AmericanRhetoric.com 

I knew his secretary, Diane Holt. We had worked together at both EEOC and Education. There 
were occasions on which I spoke to her, and on some of these occasions undoubtedly I passed 
on some casual comment to then Chairman Thomas. There were a series of calls in the first 
three months of 1985, occasioned by a group in Tulsa, which wished to have a civil rights 
conference. They wanted Judge Thomas to be the speaker and enlisted my assistance for this 
purpose. 

I did call in January and February to no effect, and finally suggested to the person directly 
involved, Susan Cahall, that she put the matter into her own hands and call directly. She did 
so in March of 1985. In connection with that March invitation, Ms. Cahall wanted conference 
materials for the seminar and some research was needed. I was asked to try to get the 
information and did attempt to do so. 

There was another call about another possible conference in the July of 1985. In August of 
1987, I was in Washington, D.C. and I did call Diane Holt. In the course of this conversation, 
she asked me how long I was going to be in town and I told her. It is recorded in the message 
as August 15. It was, in fact, August 20th. She told me about Judge Thomas's marriage and I 
did say, "Congratulate him." 

It is only after a great deal of agonizing consideration that I am able to talk of these 
unpleasant matters to anyone except my closest friends. As I've said before these last few 
days have been very trying and very hard for me, and it hasn't just been the last few days 
this week. It has actually been over a month now that I have been under the strain of this 
issue. 

Telling the world is the most difficult experience of my life, but it is very close to having to live 
through the experience that occasion this meeting. I may have used poor judgment early on 
in my relationship with this issue. I was aware, however, that telling at any point in my career 
could adversely affect my future career. And I did not want early on to burn all the bridges to 
the EEOC. 

As I said, I may have used poor judgment. Perhaps I should have taken angry or even 
militant steps, both when I was in the agency, or after I left it. But I must confess to the world 
that the course that I took seemed the better as well as the easier approach. 

I declined any comment to newspapers, but later when Senate staff asked me about these 
matters I felt I had a duty to report. I have no personal vendetta against Clarence Thomas. I 
seek only to provide the committee with information which it may regard as relevant. 

It would have been more comfortable to remain silent. I took no initiative to inform anyone. 
But when I was asked by a representative of this committee to report my experience, I felt 
that I had to tell the truth. I could not keep silent.

Transcription by Michael E. Eidenmuller.  Property of AmericanRhetoric.com.  © Copyright 2008. All rights reserved.  Page 5 


Diego’s MacBook Pro:~ diegoponce$ export GOOGLE_APPLICATION_CREDENTIALS="/Users/diegoponce/Desktop/MyCredentials.json"
Diego’s MacBook Pro:~ diegoponce$ python3 /Users/diegoponce/Desktop/googleAPI.py 
Text:  Anita Hill 

Opening Statement to the Senate Judiciary Committee 

Delivered 11 October 1991 

AUTHENTICITY CERTIFIED: Text version below transcribed directly from audio 

Note: Contains adult language and subject matter 

Ms. Hill: Mr. Chairman, Senator Thurmond, members of the committee: 

My name is Anita F. Hill, and I am a professor of law at the University of Oklahoma. I was 
born on a farm in Okmulgee County, Oklahoma, in 1956. I am the youngest of 13 children. I 
had my early education in Okmulgee County. My father, Albert Hill, is a farmer in that area. 
My mother's name is Irma Hill. She is also a farmer and a housewife. 

My childhood was one of a lot of hard work and not much money, but it was one of solid 
family affection, as represented by my parents. I was reared in a religious atmosphere in the 
Baptist faith, and I have been a member of the Antioch Baptist Church in Tulsa, Oklahoma, 
since 1983. It is a very warm part of my life at the present time. 

For my undergraduate work, I went to Oklahoma State University and graduated from there in 
1977. I am attaching to this statement a copy of my resume for further details of my 
education. 

Senator Biden: It will be included in the record as if read. 

Ms. Hill: Thank you. I graduated from the University with academic honors and proceeded to 
the Yale Law School, where I received my JD degree in 1980. Upon graduation from law 
school, I became a practicing lawyer with the Washington, DC, firm of Ward, Hardraker, and 
Ross.

Transcription by Michael E. Eidenmuller.  Property of AmericanRhetoric.com.  © Copyright 2008. All rights reserved.  Page 1 


AmericanRhetoric.com 

In 1981, I was introduced to now Judge Thomas by a mutual friend. Judge Thomas told me 
that he was anticipating a political appointment, and he asked if I would be interested in 
working with him. He was, in fact, appointed as Assistant Secretary of Education for Civil 
Rights. After he had taken that post, he asked if I would become his assistant, and I accepted 
that position. 

In my early period there, I had two major projects. The first was an article I wrote for Judge 
Thomas's signature on the education of minority students. The second was the organization of 
a seminar on high­risk students which was abandoned because Judge Thomas transferred to 
the EEOC where he became the chairman of that office. 

During this period at the Department of Education, my working relationship with Judge 
Thomas was positive. I had a good deal of responsibility and independence. I thought he 
respected my work and that he trusted my judgment. After approximately three months of 
working there, he asked me to go out socially with him. 

What happened next and telling the world about it are the two most difficult experiences of 
my life. It is only after a great deal of agonizing consideration and a great number of sleepless 
nights that I am able to talk of these unpleasant matters to anyone but my close friends. 

I declined the invitation to go out socially with him and explained to him that I thought it 
would jeopardize at what at the time I considered to be a very good working relationship. I 
had a normal social life with other men outside of the office. I believed then, as now, that 
having a social relationship with a person who was supervising my work would be ill­advised. I 
was very uncomfortable with the idea and told him so. 

I thought that by saying no and explaining my reasons my employer would abandon his social 
suggestions. However, to my regret, in the following few weeks, he continued to ask me out 
on several occasions. He pressed me to justify my reasons for saying no to him. These 
incidents took place in his office or mine. They were in the form of private conversations which 
would not have been overheard by anyone else. 

My working relationship became even more strained when Judge Thomas began to use work 
situations to discuss sex. On these occasions, he would call me into his office for reports on 
education issues and projects, or he might suggest that, because of the time pressures of his 
schedule, we go to lunch to a government cafeteria. After a brief discussion of work, he would 
turn the conversation to a discussion of sexual matters. 

His conversations were very vivid. He spoke about acts that he had seen in pornographic films 
involving such matters as women having sex with animals and films showing group sex or 
rape scenes. He talked about pornographic materials depicting individuals with large penises 
or large breasts involved in various sex acts. On several occasions, Thomas told me 
graphically of his own sexual prowess.

Transcription by Michael E. Eidenmuller.  Property of AmericanRhetoric.com.  © Copyright 2008. All rights reserved.  Page 2 


AmericanRhetoric.com 

Because I was extremely uncomfortable talking about sex with him at all, and particularly in 
such a graphic way, I told him that I did not want to talk about these subjects. I would also 
try to change the subject to education matters or to nonsexual personal matters such as his 
background or his beliefs. My efforts to change the subject were rarely successful. 

Throughout the period of these conversations, he also, from time to time, asked me for social 
engagements. My reaction to these conversations was to avoid them by eliminating 
opportunities for us to engage in extended conversations. This was difficult because at the 
time I was his only assistant at the Office of Education ­­ or Office for Civil Rights. 

During the latter part of my time at the Department of Education, the social pressures and 
any conversation of his offensive behavior ended. I began both to believe and hope that our 
working relationship could be a proper, cordial, and professional one. 

When Judge Thomas was made chair of the EEOC, I needed to face the question of whether to 
go with him. I was asked to do so, and I did. The work itself was interesting, and at that time 
it appeared that the sexual overtures which had so troubled me had ended. I also faced the 
realistic fact that I had no alternative job. While I might have gone back to private practice, 
perhaps in my old firm or at another, I was dedicated to civil rights work, and my first choice 
was to be in that field. Moreover, the Department of Education itself was a dubious venture. 
President Reagan was seeking to abolish the entire department. 

For my first months at the EEOC, where I continued to be an assistant to Judge Thomas, there 
were no sexual conversations or overtures. However, during the fall and winter of 1982, these 
began again. The comments were random and ranged from pressing me about why I didn't go 
out with him to remarks about my personal appearance. I remember his saying that some day 
I would have to tell him the real reason that I wouldn't go out with him. 

He began to show displeasure in his tone and voice and his demeanor and his continued 
pressure for an explanation. He commented on what I was wearing in terms of whether it 
made me more or less sexually attractive. The incidents occurred in his inner office at the 
EEOC. 

One of the oddest episodes I remember was an occasion in which Thomas was drinking a 
Coke in his office. He got up from the table at which we were working, went over to his desk 
to get the Coke, looked at the can and asked, "Who has pubic hair on my Coke?" On other 
occasions, he referred to the size of his own penis as being larger than normal, and he also 
spoke on some occasions of the pleasures he had given to women with oral sex. 

At this point, late 1982, I began to feel severe stress on the job. I began to be concerned that 
Clarence Thomas might take out his anger with me by degrading me or not giving me 
important assignments. I also thought that he might find an excuse for dismissing me.

Transcription by Michael E. Eidenmuller.  Property of AmericanRhetoric.com.  © Copyright 2008. All rights reserved.  Page 3 


AmericanRhetoric.com 

In January of 1983, I began looking for another job. I was handicapped because I feared that, 
if he found out, he might make it difficult for me to find other employment and I might be 
dismissed from the job I had. Another factor that made my search more difficult was that 
there was a period ­­ this was during a period of a hiring freeze in the government. In 
February 1983, I was hospitalized for five days on an emergency basis for an acute ­­ for 
acute stomach pain, which I attributed to stress on the job. 

Once out of the hospital, I became more committed to find other employment and sought 
further to minimize my contact with Thomas. This became easier when Allison Duncan 
became office director, because most of my work was then funneled through her and I had 
contact with Clarence Thomas mostly in staff meetings. 

In the spring of 1983, an opportunity to teach at Oral Roberts University opened up. I taught 
an afternoon session and seminar at Oral Roberts University. The dean of the university saw 
me teaching and inquired as to whether I would be interested in pursuing a career in teaching, 
beginning at Oral Roberts University. I agreed to take the job in large part because of my 
desire to escape the pressures I felt at the EEOC, due to Judge Thomas. 

When I informed him that I was leaving in July, I recall that his response was that now I 
would no longer have an excuse for not going out with him. I told him that I still preferred not 
to do so. At some time after that meeting, he asked if he could take me to dinner at the end 
of the term. When I declined, he assured me that the dinner was a professional courtesy only 
and not a social invitation. I reluctantly agreed to accept that invitation, but only if it was at 
the very end of a working day. 

On, as I recall, the last day of my employment at the EEOC in the summer of 1983, I did have 
dinner with Clarence Thomas. We went directly from work to a restaurant near the office. We 
talked about the work I had done, both at Education and at the EEOC. He told me that he was 
pleased with all of it except for an article and speech that I had done for him while we were at 
the Office for Civil Rights. Finally, he made a comment that I will vividly remember. He said 
that if I ever told anyone of his behavior that it would ruin his career. This was not an 
apology, nor was it an explanation. That was his last remark about the possibility of our going 
out or reference to his behavior. 

In July of 1983, I left Washington, D.C. area and I've had minimal contacts with Judge 
Clarence Thomas since. I am of course aware from the Press that some questions have been 
raised about conversations I had with Judge Clarence Thomas after I left the EEOC. From 
1983 until today, I have seen Judge Thomas only twice. On one occasion, I needed to get a 
reference from him, and on another he made a public appearance in Tulsa. 

On one occasion he called me at home and we had an inconsequential conversation. On one 
occasion he called me without reaching me, and I returned the call without reaching him, and 
nothing came of it. I have, on at least three occasions, been asked to [act] as a conduit to 
him for others.

Transcription by Michael E. Eidenmuller.  Property of AmericanRhetoric.com.  © Copyright 2008. All rights reserved.  Page 4 


AmericanRhetoric.com 

I knew his secretary, Diane Holt. We had worked together at both EEOC and Education. There 
were occasions on which I spoke to her, and on some of these occasions undoubtedly I passed 
on some casual comment to then Chairman Thomas. There were a series of calls in the first 
three months of 1985, occasioned by a group in Tulsa, which wished to have a civil rights 
conference. They wanted Judge Thomas to be the speaker and enlisted my assistance for this 
purpose. 

I did call in January and February to no effect, and finally suggested to the person directly 
involved, Susan Cahall, that she put the matter into her own hands and call directly. She did 
so in March of 1985. In connection with that March invitation, Ms. Cahall wanted conference 
materials for the seminar and some research was needed. I was asked to try to get the 
information and did attempt to do so. 

There was another call about another possible conference in the July of 1985. In August of 
1987, I was in Washington, D.C. and I did call Diane Holt. In the course of this conversation, 
she asked me how long I was going to be in town and I told her. It is recorded in the message 
as August 15. It was, in fact, August 20th. She told me about Judge Thomas's marriage and I 
did say, "Congratulate him." 

It is only after a great deal of agonizing consideration that I am able to talk of these 
unpleasant matters to anyone except my closest friends. As I've said before these last few 
days have been very trying and very hard for me, and it hasn't just been the last few days 
this week. It has actually been over a month now that I have been under the strain of this 
issue. 

Telling the world is the most difficult experience of my life, but it is very close to having to live 
through the experience that occasion this meeting. I may have used poor judgment early on 
in my relationship with this issue. I was aware, however, that telling at any point in my career 
could adversely affect my future career. And I did not want early on to burn all the bridges to 
the EEOC. 

As I said, I may have used poor judgment. Perhaps I should have taken angry or even 
militant steps, both when I was in the agency, or after I left it. But I must confess to the world 
that the course that I took seemed the better as well as the easier approach. 

I declined any comment to newspapers, but later when Senate staff asked me about these 
matters I felt I had a duty to report. I have no personal vendetta against Clarence Thomas. I 
seek only to provide the committee with information which it may regard as relevant. 

It would have been more comfortable to remain silent. I took no initiative to inform anyone. 
But when I was asked by a representative of this committee to report my experience, I felt 
that I had to tell the truth. I could not keep silent. ''', verbose = True)
