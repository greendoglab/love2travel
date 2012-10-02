# -*-coding: utf-8-*-
from feedback.forms import OrderForm
from django.core.context_processors import csrf
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.core.mail import send_mail

def feedback(request):
    if request.method == 'POST': # If the form has been submitted...
        form = OrderForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass

            name =  form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            date_married = form.cleaned_data['date_married']
            date_tour = form.cleaned_data['date_tour']
            country = form.cleaned_data['country']
            budget = form.cleaned_data['budget']
            hotel_stars = form.cleaned_data['hotel_stars']
            guest = form.cleaned_data['guest']
            best_place = form.cleaned_data['best_place']
            best_country = form.cleaned_data['best_country']
            full_budget = form.cleaned_data['full_budget']

            type_tour = form.cleaned_data['type_tour']
            fly_class = form.cleaned_data['fly_class']
            eat_hotel = form.cleaned_data['eat_hotel']
            guest_pay = form.cleaned_data['guest_pay']
            advance = form.cleaned_data['advance']

            message = form.cleaned_data['message']
            cc_myself = form.cleaned_data['cc_myself']

            from_email = email
            subject = u'Письмо с сайта LOVE2TRAVEL jn %s' % name
            mail_message = u'Имя: %s \n Телефон: %s \n Почта: %s \n  Текст: %s \n \
            Дата свадьбы: %s \n Дата тура: %s \n Страна: %s \n Бюджет: %s \n Звезды отелея: %s \n \
            Гости: %s \n Лучшее место: %s \n Лучшая страна: %s \n Полный бюджет: %s \n \
            тип тура: %s \n Класс перелета: %s \n Еда в отеле: %s \n Гости платят: %s \n дополнительно: %s \n' \
            % (name, phone, email, message, date_married, date_tour, country, budget, hotel_stars, \
                 guest, best_place, best_country, full_budget, type_tour, fly_class, eat_hotel, guest_pay, \
                 advance)

            recipients = ['info@love2travel.com.ua', 'fontanii@gmail.com']
            if cc_myself:
                recipients.append(email)

            send_mail(subject, mail_message, from_email, recipients)
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = OrderForm() # An unbound form

    return render_to_response('order.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def thanks(request):
    return render_to_response('thanks.html',{
        'thanks' : u'Спасибо что связались с нами! Мы ответим вам в ближайшее время.',
    })