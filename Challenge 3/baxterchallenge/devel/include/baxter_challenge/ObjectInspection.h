// Generated by gencpp from file baxter_challenge/ObjectInspection.msg
// DO NOT EDIT!


#ifndef BAXTER_CHALLENGE_MESSAGE_OBJECTINSPECTION_H
#define BAXTER_CHALLENGE_MESSAGE_OBJECTINSPECTION_H

#include <ros/service_traits.h>


#include <baxter_challenge/ObjectInspectionRequest.h>
#include <baxter_challenge/ObjectInspectionResponse.h>


namespace baxter_challenge
{

struct ObjectInspection
{

typedef ObjectInspectionRequest Request;
typedef ObjectInspectionResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct ObjectInspection
} // namespace baxter_challenge


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::baxter_challenge::ObjectInspection > {
  static const char* value()
  {
    return "b7b93667ab19d45333d9d3fab6d6a1fb";
  }

  static const char* value(const ::baxter_challenge::ObjectInspection&) { return value(); }
};

template<>
struct DataType< ::baxter_challenge::ObjectInspection > {
  static const char* value()
  {
    return "baxter_challenge/ObjectInspection";
  }

  static const char* value(const ::baxter_challenge::ObjectInspection&) { return value(); }
};


// service_traits::MD5Sum< ::baxter_challenge::ObjectInspectionRequest> should match 
// service_traits::MD5Sum< ::baxter_challenge::ObjectInspection > 
template<>
struct MD5Sum< ::baxter_challenge::ObjectInspectionRequest>
{
  static const char* value()
  {
    return MD5Sum< ::baxter_challenge::ObjectInspection >::value();
  }
  static const char* value(const ::baxter_challenge::ObjectInspectionRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::baxter_challenge::ObjectInspectionRequest> should match 
// service_traits::DataType< ::baxter_challenge::ObjectInspection > 
template<>
struct DataType< ::baxter_challenge::ObjectInspectionRequest>
{
  static const char* value()
  {
    return DataType< ::baxter_challenge::ObjectInspection >::value();
  }
  static const char* value(const ::baxter_challenge::ObjectInspectionRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::baxter_challenge::ObjectInspectionResponse> should match 
// service_traits::MD5Sum< ::baxter_challenge::ObjectInspection > 
template<>
struct MD5Sum< ::baxter_challenge::ObjectInspectionResponse>
{
  static const char* value()
  {
    return MD5Sum< ::baxter_challenge::ObjectInspection >::value();
  }
  static const char* value(const ::baxter_challenge::ObjectInspectionResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::baxter_challenge::ObjectInspectionResponse> should match 
// service_traits::DataType< ::baxter_challenge::ObjectInspection > 
template<>
struct DataType< ::baxter_challenge::ObjectInspectionResponse>
{
  static const char* value()
  {
    return DataType< ::baxter_challenge::ObjectInspection >::value();
  }
  static const char* value(const ::baxter_challenge::ObjectInspectionResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // BAXTER_CHALLENGE_MESSAGE_OBJECTINSPECTION_H
